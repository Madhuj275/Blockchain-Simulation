from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Block
import time

@api_view(['GET'])
def get_chain(request):
    chain = Block.objects.all().order_by('index')
    return Response([{
        'index': block.index,
        'transactions': block.transactions,
        'previous_hash': block.previous_hash,
        'hash': block.hash,
        'nonce': block.nonce
    } for block in chain])

@api_view(['POST'])
def add_transaction(request):
    transactions = request.data.get('transactions', [])
    if not transactions:
        return Response({"error": "No transactions provided"}, status=status.HTTP_400_BAD_REQUEST)

    last_block = Block.objects.last()
    new_block = Block(
        transactions=transactions,
        previous_hash=last_block.hash if last_block else '0',
        timestamp=time.time()
    )

    # Proof-of-Work
    difficulty = 4
    while True:
        new_block.hash = new_block.calculate_hash()
        if new_block.hash.startswith('0' * difficulty):
            break
        new_block.nonce += 1

    new_block.save()
    return Response({"message": "Block added successfully"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def tamper_block(request, index):
    try:
        block = Block.objects.get(index=index)
    except Block.DoesNotExist:
        return Response({"error": "Block not found"}, status=status.HTTP_404_NOT_FOUND)

    block.transactions = request.data.get('transactions', block.transactions)
    block.save()
    return Response({"message": "Block tampered successfully"})

@api_view(['GET'])
def validate_chain(request):
    chain = Block.objects.all().order_by('index')
    is_valid = True

    for i in range(1, len(chain)):
        current = chain[i]
        previous = chain[i-1]

        if current.hash != current.calculate_hash():
            is_valid = False
        if current.previous_hash != previous.hash:
            is_valid = False

    return Response({"is_valid": is_valid})