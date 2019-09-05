import Pyro4

@Pyro4.expose
class ChineseCheckers():
    mensages = []
    player_color = "RED"
    players = []

    def get_mensages(self):
        if len(self.mensages) == 11:
            self.mensages.pop(0)
        return self.mensages

    def set_new_mensage(self, mensage):
        print(f"mensage from:{self.player_color} : {mensage}")
        self.mensages.append((self.player_color, mensage))

    def join_server(self):
        if len(self.players) == 0:
            self.players.append("RED")
        elif self.players[0] == "GREEN":
            self.players.insert(0,"RED")
        else:
            self.players.append("GREEN")
            self.player_color = "GREEN"
        self.set_new_mensage("conectou-se")

    def exit_server(self):
        self.set_new_mensage("desconectou!")
        self.players.remove(self.player_color)


daemon = Pyro4.Daemon()
uri = daemon.register(ChineseCheckers)
ns = Pyro4.locateNS()
ns.register("obj",uri)

daemon.requestLoop()
