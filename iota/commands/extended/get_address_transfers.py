# coding=utf-8
from __future__ import absolute_import, division, print_function, \
  unicode_literals

from itertools import chain
from typing import Optional

import filters as f
from iota.commands import FilterCommand, RequestFilter
from iota.commands.core.find_transactions import FindTransactionsCommand
from iota.commands.extended.utils import get_bundles_from_transaction_hashes, \
  iter_used_addresses
from iota.crypto.addresses import AddressGenerator
from iota.crypto.types import Seed
from iota.filters import Trytes

__all__ = [
  'GetAddressTransfersCommand',
]


class GetAddressTransfersCommand(FilterCommand):
  """
  Executes ``getAddressTransfers`` extended API command.
  See :py:meth:`iota.api.Iota.get_transfers` for more info.
  """
  command = 'getAddressTransfers'

  def get_request_filter(self):
    pass

  def get_response_filter(self):
    pass

  def _execute(self, request):
    inclusion_states  = request['inclusionStates'] # type: bool
    address              = request['address'] # type: Address

    # Determine the addresses we will be scanning, and pull their
    # transaction hashes.

    ft_response =\
        FindTransactionsCommand(self.adapter)(
            addresses =
                address
        )

    my_hashes = ft_response['hashes']

    return {
      'bundles':
        get_bundles_from_transaction_hashes(
          adapter             = self.adapter,
          transaction_hashes  = my_hashes,
          inclusion_states    = inclusion_states,
        ),
    }
