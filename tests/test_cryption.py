from cryption import decrypthash, encryptstring, make_keys


def test_encrypt_decrypt_sequence_using_make_keys():
    keys = make_keys()
    encoded_hash = encryptstring(
        keys.public, 'The quick brown fox jumped over the lazy dog')
    decryptedtext = decrypthash(keys.private, encoded_hash)
    assert 'The quick brown fox jumped over the lazy dog' == decryptedtext
