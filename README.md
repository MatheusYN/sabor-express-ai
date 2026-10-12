# Sabor Express AI

## Rota Inteligente: Otimização de Entregas com Algoritmos de IA

**Projeto acadêmico de Inteligência Artificial**

## 1. Descrição do problema

O Sabor Express AI é um protótipo de sistema para apoiar o planejamento de entregas de uma empresa fictícia de delivery. O objetivo é encontrar caminhos de menor distância entre o restaurante e os destinos, organizar entregas por proximidade geográfica e apresentar os resultados por meio de gráficos.

A solução utiliza uma rede de locais conectados por vias com distâncias simuladas. Os dados foram criados exclusivamente para fins acadêmicos e não representam ruas ou distâncias reais.

## 2. Objetivos

* Encontrar rotas de menor custo entre dois locais.
* Comparar os algoritmos A* e Dijkstra.
* Agrupar destinos utilizando K-Means.
* Gerar gráficos para facilitar a interpretação dos resultados.
* Validar as funcionalidades com testes automatizados.

## 3. Tecnologias utilizadas

* Python 3
* NetworkX
* Matplotlib
* scikit-learn
* CSV para armazenamento dos dados
* unittest para testes automatizados
* Git e GitHub para versionamento e publicação

## 4. Estrutura do projeto

```text
sabor-express-ai/
├── data/
│   ├── locations.csv
│   ├── roads.csv
│   └── deliveries.csv
├── src/
│   ├── main.py
│   ├── graph.py
│   ├── astar.py
│   ├── dijkstra.py
│   ├── clustering.py
│   └── visualization.py
├── tests/
│   └── test_algorithms.py
├── outputs/
│   ├── rota_astar.png
│   └── grupos_kmeans.png
├── README.md
├── requirements.txt
└── .gitignore
```

## 5. Algoritmos implementados

### A*

O A* utiliza o custo acumulado do percurso e uma heurística para orientar a busca em direção ao destino. Neste projeto, a heurística é baseada na distância euclidiana entre as coordenadas simuladas dos locais.

### Dijkstra

O algoritmo de Dijkstra calcula caminhos de menor custo em grafos com pesos não negativos. Foi utilizado como referência para comparar o resultado do A*.

### K-Means

O K-Means agrupa os pontos de entrega de acordo com suas coordenadas. O projeto utiliza três grupos e uma configuração reprodutível, com `random_state=42`.

O agrupamento identifica regiões geográficas, mas não define, por si só, a melhor sequência de visitas nem resolve integralmente o problema de roteamento de múltiplos veículos.

## 6. Como executar o projeto

### Pré-requisitos

* Python instalado.
* Git instalado, caso queira clonar o repositório.

### Instalação

Clone o repositório:

```bash
git clone URL_DO_SEU_REPOSITORIO
cd sabor-express-ai
```

Crie e ative um ambiente virtual no Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o programa:

```bash
python src/main.py
```

Execute os testes:

```bash
python -m unittest discover -s tests -v
```

Substitua `URL_DO_SEU_REPOSITORIO` pelo endereço real do repositório depois de publicá-lo no GitHub.

## 7. Resultados obtidos

Na execução de referência, o A* e o Dijkstra encontraram a rota:

**A → B → D → G → H → J**

A distância total calculada foi de **10,472 unidades de distância**, interpretadas como quilômetros apenas para fins de simulação.

Os dois algoritmos encontraram o mesmo custo para esse percurso. Os testes automatizados também verificaram a igualdade dos custos, os pontos inicial e final da rota e a formação de três grupos contendo as nove entregas.

### Evidências visuais

O programa gera os seguintes arquivos na pasta `outputs`:

* `rota_astar.png`: representação da rede e destaque do percurso calculado.
* `grupos_kmeans.png`: representação dos agrupamentos geográficos das entregas.

## 8. Eficiência e limitações

O A* utiliza uma heurística para orientar a exploração do grafo, enquanto Dijkstra prioriza os custos acumulados. O desempenho efetivo depende do tamanho e da estrutura da rede e da qualidade da heurística.

O K-Means permite visualizar regiões de entrega, mas não garante uma rota globalmente ótima para múltiplas entregas.

As principais limitações do protótipo são:

* Dados e distâncias simulados.
* Ausência de informações reais de trânsito.
* Ausência de janelas de entrega e capacidade dos veículos.
* Ausência de otimização completa de múltiplas paradas.
* Ausência de integração com mapas ou serviços externos.

## 9. Melhorias futuras

Como evolução, o projeto poderá incorporar dados geográficos reais, restrições de tempo, capacidade dos veículos, comparação de desempenho em grafos maiores e algoritmos específicos de roteamento de veículos, como variantes do Vehicle Routing Problem (VRP).

## 10. Conclusão

O projeto demonstra a aplicação prática de algoritmos de busca em grafos e aprendizado não supervisionado para apoiar o planejamento de entregas. A comparação entre A* e Dijkstra permitiu validar o custo da rota testada, enquanto o K-Means possibilitou agrupar os destinos por proximidade geográfica.

Os testes automatizados e os gráficos complementam a implementação e facilitam a verificação dos resultados. Apesar das limitações da simulação, a solução oferece uma base organizada para futuras melhorias no planejamento logístico.

## 11. Autor

Matheus Yoshihiro Nishiyama
