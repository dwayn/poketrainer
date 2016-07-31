


class TransferHelper(object):
    """"TransferHelpers are intended to identify pokemon that should be transferred"""

    def __init__(self, config, filtered={}):
        self.processConfig(config)

    def processConfig(self, config, filtered={}):
        """this can be overridden in subclasses if there is any post processing that is needed

            Args:
                config      :config object, at a minimum this should be a dict
                filtered    (dict): should be a dict mapping filter name to a list of pokemon that it filtered

        """
        self.config = config
        self.filtered = filtered

    def getPokemonToTransfer(self, pokemonId, pokemons):
        """Goes through the list of all pokemon of a given pokemonId and returns a list of pokemon to transfer

            Args:
                pokemonId   (int): integer pokemon id
                pokemons    (list): list of all the caught pokemon of given pokemon id

            Returns:
                (list, list): first list is pokemon that are slated for transfer, second list is pokemon that are not to be transferred
        """
        raise NotImplemented("getTransferrablePokemon() must be implemented in all transfer helpers")


class TransferFilter(object):
    """TransferFilters are intended to filter a list of pokemon and remove the ones that should be kept"""

    def __init__(self, config):
        self.processConfig(config)

    def processConfig(self, config):
        """this can be overridden in subclasses if there is any post processing that is needed"""
        self.config = config

    def filterPokemon(self, pokemonId, pokemons):
        """Goes through the list of all pokemon of a given pokemonId and filters out the pokemon that should be kept so
        that the remaining can be processed by TransferHelpers

            Args:
                pokemonId   (int): integer pokemon id
                pokemons    (list): list of all the caught pokemon of given pokemon id

            Returns:
                (list, list): first list is pokemon still eligible to be transferred, second list is pokemon that were filtered out
        """
        raise NotImplemented("getTransferrablePokemon() must be implemented in all transfer helpers")
