from hashlib import sha256
MAX_NONCE = 1000000


def SHA256(text):
    return sha256(text.encode('ascii')).hexdigest()


def mine(block_number, transaction, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number)+transaction+previous_hash+str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print('Yay! Successfully mined bitcoin with nonce:', nonce)
            return new_hash

    raise Exception('Failed to mine bitcoin', MAX_NONCE)


if __name__ == '__main__':
    transaction = '''
    Dhaval->Rohan: 100,000
    Rohan->Dhaval: 200,000

    '''
    dificiality = 4
    new_hash = mine(
        5, transaction, 'b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78', dificiality)

    print(new_hash)
