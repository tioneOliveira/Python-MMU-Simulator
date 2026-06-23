class PageTableEntry:  # Estrutura para lidar com as entradas das tabelas.
    def __init__(self):
        self.valid = False
        self.frame_number = -1

    def __str__(self):
        return str(self.frame_number) if self.frame_number != -1 else ""


class MMU:
    def __init__(self):
        # Especificações do sistema,
        self.PAGE_SIZE = 8192
        self.PHYSICAL_MEMORY = 65536
        self.VIRTUAL_MEMORY = 1048576

        # Derivações das especificações.
        self.NUM_FRAMES = self.PHYSICAL_MEMORY // self.PAGE_SIZE
        self.NUM_PAGES = self.VIRTUAL_MEMORY // self.PAGE_SIZE

        # List iteration para preencher a tabela de páginas.
        self.page_table = [PageTableEntry() for _ in range(self.NUM_PAGES)]
        self.physical_memory = [-1] * self.NUM_FRAMES

        # Usaremos uma Least Recently Used (LRU) para tratar substituição.
        # O ínico da lista indica o item mais antigo a ser acessado, o fim indica o mais recente.
        self.lru_list = []
        self.frames_used = 0

    def access_address(self, process_id, virtual_address):
        print(f"\nPID {process_id}: solicita endereço virtual {virtual_address}")

        # Calculo do indice da página.
        page_number = virtual_address // self.PAGE_SIZE
        offset = virtual_address % self.PAGE_SIZE
        print(f"Página: {page_number} | Deslocamento: {offset}")

        # Caso já esteja em memória, só calcula o endereço físico e mostra junto com o frame.
        if self.page_table[page_number].valid:
            # Funçãozinha para melhorar leitura.
            self._calculate_physical_adress(page_number, offset)
            # Como foi acessado, atualiza a posição na LRU.
            self.lru_list.remove(page_number)
            self.lru_list.append(page_number)

        # Caso não esteja na memória física, MMU emite page fault.
        else:
            print("MMU: FALTA DE PÁGINA!")
            self._handle_page_fault(page_number)
            print("Página carregada:")
            self._calculate_physical_adress(page_number, offset)

    def _handle_page_fault(self, page_number):
        # Verifica se a memória física está cheia.
        if self.frames_used < self.NUM_FRAMES:
            # Seleciona o primeiro frame disponível.
            target_frame = self.frames_used
            self.frames_used += 1
            print(f"Frame livre encontrado ({target_frame}).")

        # Se não há um frame livre, usamos a LRU.
        else:
            print("MEMÓRIA CHEIA!")
            # Retiramos o primeiro item da LRU, o item mais antigo a ser acessado.
            old_page = self.lru_list.pop(0)
            target_frame = self.page_table[old_page].frame_number

            # Setamos na tabela de páginas que o item do inicio da LRU não está mais em memória física.
            self.page_table[old_page].valid = False
            self.page_table[old_page].frame_number = -1

            print(
                f"A página {old_page}, presente no frame {target_frame}, foi substituída pela página {page_number}."
            )

        # Setamos na tabela de página que o item agora está em memória principal.
        self.physical_memory[target_frame] = page_number
        self.page_table[page_number].valid = True
        self.page_table[page_number].frame_number = target_frame

        # Foi acessado, é posto no fim da LRU.
        self.lru_list.append(page_number)

    def _calculate_physical_adress(self, page_number, offset):
        frame = self.page_table[page_number].frame_number
        physical_address = (frame * self.PAGE_SIZE) + offset
        print(f"Endereço Físico: {physical_address} | Frame: {frame}")

    def __str__(self):
        page_table_str = ""
        for j, i in enumerate(self.page_table, start=1):
            if i.frame_number in self.physical_memory and i.frame_number != -1:
                page_table_str += f"{j}: {i}\n"
        return f"++ MMU ++\nTábela de páginas:\n{page_table_str}Memória física: {self.physical_memory}"


if __name__ == "__main__":
    mmu = MMU()

    mmu.access_address(1, 5000)
    print("\n")
    print(mmu)
    print("=================================")

    mmu.access_address(1, 15000)
    print("\n")
    print(mmu)
    print("=================================")

    mmu.access_address(1, 25000)
    print("\n")
    print(mmu)
    print("=================================")

    mmu.access_address(1, 35000)
    print("\n")
    print(mmu)
    print("=================================")
    print("=================================")
    print("=================================")

    mmu.access_address(2, 45000)
    print("\n")
    print(mmu)
    print("=================================")

    mmu.access_address(2, 55000)
    print("\n")
    print(mmu)
    print("=================================")

    mmu.access_address(2, 65000)
    print("\n")
    print(mmu)
    print("=================================")

    mmu.access_address(2, 75000)
    print("\n")
    print(mmu)
    print("=================================")
    print("=================================")

    mmu.access_address(1, 5000)
    print("\n")
    print(mmu)
    print("=================================")
    print("=================================")

    mmu.access_address(2, 85000)
    print("\n")
    print(mmu)
