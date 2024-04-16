from pythonping import ping as ping_function

class Ping:
    def execute(self, ip_address: str) -> None:
        if not ip_address.startswith("192."):
            print("Ping: Dirección IP inválida. Debe comenzar con '192.'")
            return

        print(f"Ping: Ejecutando ping a {ip_address}")
        for i in range(1, 11):
            try:
                resultado = ping_function(ip_address, count=1)
                print(f"Resultado del ping para el intento {i}:")
                print(resultado)
            except Exception as e:
                print(f"Error al ejecutar el ping: {e}")

    def executefree(self, ip_address: str) -> None:
        print(f"Ping: Ejecutando ping a {ip_address}")
        for i in range(1, 11):
            try:
                resultado = ping_function(ip_address, count=1)
                print(f"Resultado del ping para el intento {i}:")
                print(resultado)
            except Exception as e:
                print(f"Error al ejecutar el ping: {e}")

class PingProxyAdapter(Ping):
    def __init__(self, ping: Ping) -> None:
        self._ping = ping

    def execute(self, ip_address: str) -> None:
        if ip_address == "192.168.0.254":
            print("PingProxy: Redirigiendo al método executefree.")
            self._ping.executefree("www.google.com")
        else:
            print("PingProxy: Redirigiendo al método execute de Ping.")
            self._ping.execute(ip_address)

if __name__ == "__main__":
    print("Cliente: Ejecutando el código de cliente con Ping:")
    ping = Ping()
    ping.execute("192.0.2.1")  
    print("")

    print("Cliente: Ejecutando el código de cliente con PingProxy:")
    proxy = PingProxyAdapter(Ping())
    proxy.execute("192.0.2.1")  
    print("")

    print("Cliente: Ejecutando el código de cliente con PingProxy para el caso especial:")
    proxy.execute("192.168.0.254")
