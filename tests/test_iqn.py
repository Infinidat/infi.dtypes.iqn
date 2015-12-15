from infi.dtypes.iqn import IQN

def test_basic():
    a = IQN('iqn.2001-04.com.example:storage:diskarrays-sn-a8675309')
    assert hash(a) == hash('iqn.2001-04.com.example:storage:diskarrays-sn-a8675309')
    assert a == a
    assert a == 'iqn.2001-04.com.example:storage:diskarrays-sn-a8675309'
    assert a != 'lol'
    assert a.get_date() == '2001-04'
    assert a.get_naming_authority() == 'com.example'
    assert a.get_extra() == 'storage:diskarrays-sn-a8675309'
    assert a.get_extra_fields() == ('storage', 'diskarrays-sn-a8675309')

def test_rfc_examples():
    a = IQN('iqn.2001-04.com.example')
    assert a.get_date() == '2001-04'
    assert a.get_naming_authority() == 'com.example'
    assert a.get_extra() == ''
    assert a.get_extra_fields() == ()

def test_copy_ctor():
    a = IQN('iqn.2001-04.com.example')
    assert IQN(a) == a
