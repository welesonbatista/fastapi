import asyncio


async def tarefa(nome, duracao):
  print(f"Tarefa {nome} iniciada.")
  await asyncio.sleep(duracao)
  print(f"Tarefa {nome} concluída após {duracao} segundos.")


#corrotina
async def main():
  await asyncio.gather(
    tarefa("A", 3),
    tarefa("B", 6)
  )
  await tarefa("C", 4)

if __name__ == "__main__":
  asyncio.run(main())
