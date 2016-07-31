import base
from pgoapi.protos.POGOProtos import Enums_pb2


class FavoriteFilter(base.TransferHelper):
    """filters out any pokemon that has been favorited"""

    def filterPokemon(self, pokemonId, pokemons):
        eligible = []
        notEligible = []
        for pokemon in pokemons:
            if pokemon.is_favorite:
                notEligible.append(pokemon)
            else:
                eligible.append(pokemon)
        return eligible, notEligible


class KeepCPOverFilter(base.TransferFilter):
    """filters out pokemon with CP > KEEP_CP_OVER"""

    def filterPokemon(self, pokemonId, pokemons):
        eligible = []
        notEligible = []
        for pokemon in pokemons:
            if pokemon.cp > self.config.get('KEEP_CP_OVER', 0):
                notEligible.append(pokemon)
            else:
                eligible.append(pokemon)
        return eligible, notEligible


class KeepIVOverFilter(base.TransferFilter):
    """filters out pokemon with IV > KEEP_IV_OVER"""

    def filterPokemon(self, pokemonId, pokemons):
        eligible = []
        notEligible = []
        for pokemon in pokemons:
            if pokemon.cp > self.config.get('KEEP_IV_OVER', 0):
                notEligible.append(pokemon)
            else:
                eligible.append(pokemon)
        return eligible, notEligible


class KeepPokemonIdsFilter(base.TransferFilter):
    """filters out all pokemon that are in the list of pokemon to keep"""
    def processConfig(self, config):
        self.config = config
        self.keep_pokemon_ids = map(lambda x: getattr(Enums_pb2, x), config.get("KEEP_POKEMON_NAMES", []))

    def filterPokemon(self, pokemonId, pokemons):
        if pokemonId in self.keep_pokemon_ids:
            return pokemons, []
        return [], pokemons


class StandardTransferHelper(base.TransferHelper):

    def processConfig(self, config, filtered={}):
        self.config = config
        self.filtered = filtered




    def getPokemonToTransfer(self, pokemonId, pokemons):
        kept_pokemon_of_type = 0
        kept_pokemon_of_type_high_iv = 0
        for filterName, filtered in self.filtered.iteritems():
            kept_pokemon_of_type += len(filtered)
            if filterName == 'pgoapi.transfer.classic.KeepIVOverFilter':
                kept_pokemon_of_type_high_iv += 1



        pass







