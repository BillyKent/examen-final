import time


def decorador_tiempo_ejecucion(funcionB):
    def funcionC(*args, **kwargs):
        timestamp = time.time()
        funcionB(*args, **kwargs)
        ellapsed_time = time.time() - timestamp
        return ellapsed_time

    return funcionC


@decorador_tiempo_ejecucion
def dividir_numeros(a, b):
    # Simular demora
    time.sleep(1)
    return a / b


print("Tiempo total transcurrido:", dividir_numeros(8, 2))
