import ants, importlib
importlib.reload(ants)
beehive = ants.Hive(ants.AssaultPlan())
dimensions = (2, 9)
gamestate = ants.GameState(None, beehive, ants.ant_types(),
         ants.dry_layout, dimensions)
#
# Adding/Removing QueenAnt with Container
place = gamestate.places['tunnel_0_3']
queen = ants.QueenAnt()
impostor = ants.QueenAnt()
container = ants.TankAnt()
place.add_insect(container)
place.add_insect(impostor)
impostor.action(gamestate)
place.ant is container
#True
container.place is place
#True
container.contained_ant is None
True
impostor.place is None
True
place.add_insect(queen)
place.remove_insect(queen)
container.contained_ant is queen
False

