class Listener(object):
  def __init__(self,api):
    self.api = api
  def releasePokemonById(self, p_id):
    return self.api.do_release_pokemon_by_id(p_id)
  def current_location(self):
    print self.api._posf
    return self.api._posf
  def getCaughtPokemons(self):
    return self.api.get_caught_pokemons(as_json=True)
  def getInventory(self):
    return self.api.get_player_inventory(as_json=True)
  def getPlayerInfo(self):
    return self.api.get_player_info()
  def ping(self):
    return "pong"
