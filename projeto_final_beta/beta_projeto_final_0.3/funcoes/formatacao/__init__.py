from decimal import Decimal
from rich import print as rprint
from rich.box import ROUNDED
from rich.table import Table

def mensagem(msg):
    tamanho = len(msg) + 6
    print('='* tamanho)
    print(f'{msg:^{tamanho}}')
    print('='* tamanho)


def formatar_real(valor: Decimal) -> str:
    """Formata um valor Decimal para a representação em Real (R$)."""
    return f"R$ {valor:.2f}".replace('.', ',')


def mostrar_tabela(tabela, titulo, *colunas, moeda=-1):
    """Mostra uma tabela utilizando rich, com formatação específica para valores."""
    table = Table(title=titulo, box=ROUNDED, header_style="bold blue")
    for coluna in colunas:
        table.add_column(f"[cyan]{coluna}[/cyan]", justify="right")
    for linha in tabela:
        linha_formatada = list(linha)
        if linha_formatada and isinstance(linha_formatada[moeda], Decimal):
            linha_formatada[moeda] = formatar_real(linha_formatada[moeda])
        table.add_row(*[str(dado) for dado in linha_formatada])
    rprint(table)