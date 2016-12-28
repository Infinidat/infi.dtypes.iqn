import pytest
import itertools
from infi.dtypes.iqn import IQN, iSCSIName, InvalidIQN, make_iscsi_name  # pylint: disable=no-name-in-module


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


@pytest.mark.parametrize('copy_types', itertools.product([IQN, iSCSIName], repeat=2))
def test_copy_ctor(copy_types):
    source_type, target_type = copy_types
    obj = source_type('iqn.2001-04.com.example')
    assert target_type(obj) == obj


def test_invalid_iqn():
    iscsi_identifier = '1'
    with pytest.raises(InvalidIQN):
        IQN(iscsi_identifier)
    iSCSIName(iscsi_identifier)
    assert isinstance(make_iscsi_name(iscsi_identifier), iSCSIName)


def test_equality():
    iscsi_identifier = 'iqn.2001-04.com.example'
    iqn = IQN(iscsi_identifier)
    iscsi_name = iSCSIName(iscsi_identifier)
    assert iqn == iscsi_name
    assert iqn == iscsi_identifier
    assert iscsi_name == iqn
    assert iscsi_name == iscsi_identifier
