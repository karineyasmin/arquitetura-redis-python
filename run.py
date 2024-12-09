from datetime import datetime
from configs.start_form import start_form
from models.redis.connection.redis_connection import RedisConnectionHandle
from models.redis.redis_repository import RedisRepository

redis_conn = RedisConnectionHandle().connect()
redis_repository = RedisRepository(redis_conn)
# redis_repository.insert("Estou", "AQUIIII!!!!!!!")
# value = redis_repository.get("Estou")
# print(value)

# redis_repository.insert_hash("MeuHash", "campo_1", "Este e meu valor")
# val = redis_repository.get_hash("MeuHash", "campo_1")
# print(val)


# redis_repository.insert_ex("Chave_com_ex", "vai_expirar", 30)
data_atual = datetime.now()
data_formatada = data_atual.strftime("%Y-%m-%d")
hash_items = redis_conn.hgetall(data_formatada)
print(hash_items)


# redis_repository.insert_hash_ex(data_formatada, "banana", 3.12, 40)
# redis_repository.insert_hash(data_formatada, "morango", 4.90)
# redis_repository.insert_hash(data_formatada, "uva", 8.00)

# 2. Carregar dados ao formulario
python_dict = {}
for key, value in hash_items.items():
    python_dict[key.decode("utf-8")] = value.decode("utf-8")
print(python_dict)
start_form.load_info(python_dict)

# 3. Utilizar valor armazenado
value = start_form.get_info("morango")
print(value)
