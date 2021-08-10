from storages.backends.azure_storage import AzureStorage

class PublicAzureStorage(AzureStorage):
    account_name = 'https://ajoubertdjangostorage.blob.core.windows.net/'
    account_key = '38PN+jwoSHV/W2pM4k7eB0BpAsChbafFxUSMioHNmrgMgo+zm2B7WQRvlzYUnnODZQZ7WoILnEG9XWg4VJSOkg=='
    azure_container = 'djangostatic'
    expiration_secs = None
