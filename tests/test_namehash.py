from __future__ import unicode_literals

import pytest

import codecs

from namehash import namehash


@pytest.mark.parametrize(
    'name,expected_as_hex',
    (
        ('', b'0000000000000000000000000000000000000000000000000000000000000000'),
        ('eth', b'93cdeb708b7545dc668eb9280176169d1c33cfd8ed6f04690a0bcc88a93fc4ae'),
        ('foo.eth', b'de9b09fd7c5f901e23a3f19fecc54828e9c848539801e86591bd9801b019f84f'),
        (b'', b'0000000000000000000000000000000000000000000000000000000000000000'),
        (b'eth', b'93cdeb708b7545dc668eb9280176169d1c33cfd8ed6f04690a0bcc88a93fc4ae'),
        (b'foo.eth', b'de9b09fd7c5f901e23a3f19fecc54828e9c848539801e86591bd9801b019f84f'),
    )
)
def test_namehash(name, expected_as_hex):
    actual = namehash(name)
    actual_as_hex = codecs.encode(namehash(name), 'hex')
    assert actual_as_hex == expected_as_hex
