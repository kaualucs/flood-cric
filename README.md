# 📖 Documentação do Projeto: Análise e Processamento de Dados Hidrográficos 🗺️

Este projeto foi desenvolvido para a análise e o processamento de dados geoespaciais utilizando a **Base Hidrográfica Otto-codificada Multiescalas 2017 - Ottobacias Níveis 1 a 7**. A iniciativa visa extrair e converter informações de áreas de contribuição hidrográfica, aplicando a metodologia de **Otto Pfafstetter** para a codificação e organização das bacias.

O projeto se concentra no uso de dados geoespaciais representados em geopackages (`.gpkg`) e na conversão de arquivos de pontos em KML para o formato CSV, permitindo análises subsequentes em outras plataformas.

---

### 🔬 Metodologia e Conceitos Técnicos

A metodologia de **Otto Pfafstetter** é a base para a codificação das bacias hidrográficas. A codificação se dá de jusante (rio abaixo) para montante (rio acima). Os quatro afluentes com maior área de drenagem de um rio principal recebem os números pares 2, 4, 6 e 8. Os afluentes menores são agrupados em interbacias, que recebem os números ímpares 1, 3, 5, 7 e 9.

* **Sistema de Coordenadas Geográficas**: Os dados estão no sistema **SIRGAS 2000 (SRID 4674)**.
* **Projeções**: Para os cálculos, diferentes projeções são aplicadas:
    * **Projeção Equivalente de Albers**: Utilizada para o cálculo de áreas de bacia, com a unidade de trabalho em quilômetros quadrados ($km^2$).
    * **Projeção Policônica (SRID 5880)**: Utilizada para o cálculo de extensões, com a unidade de trabalho em quilômetros.

---

### 📁 Estrutura do Repositório

* **`main.py`**: O script principal que orquestra as operações. Ele é responsável por ler o arquivo geopackage e chamar a função de conversão de KML para CSV.
* **`dados/`**: Diretório que armazena os dados de entrada e saída.
    * `geoft_bho_ach_otto_nivel_07.gpkg`: O arquivo GeoPackage que representa as áreas de contribuição hidrográfica.
    * `pontos_sirgas2000.csv`: O arquivo de saída no formato CSV, gerado a partir do KML de entrada.
* **`AreaDelimitada.kml`**: O arquivo de entrada no formato KML que contém os pontos geográficos a serem processados.
* **`.gitignore`**: Configurado para ignorar arquivos grandes, como o `geoft_bho_ach_otto_nivel_07.gpkg`.

---

### 🛠️ Instalação e Execução

Para rodar este projeto, certifique-se de ter as dependências Python necessárias, como `geopandas` e `fiona`.

1.  Clone o repositório para o seu ambiente local.
2.  Posicione o arquivo da base de dados (`geoft_bho_ach_otto_nivel_07.gpkg`) dentro do diretório `dados/`.
3.  Execute o script principal a partir da linha de comando:
    ```bash
    python main.py
    ```
    A execução do script converterá o arquivo KML de entrada e salvará o resultado em `dados/pontos_sirgas2000.csv`.

---

### 📊 Campos de Dados

O geopackage **`GEOFT_BHO_ACH_OTTO_NIVEL_n`** possui os seguintes campos relevantes para análise:

* **`fid`**: Identificação única do registro.
* **`wts_pk`**: Identificação única do registro.
* **`wts_cd_pfafstetterbasin`**: Codificação de bacias hidrográficas de Pfafstetter.
* **`wts_cd_pfafstetterbasincodelevel`**: Nível da codificação de bacias hidrográficas de Pfafstetter.
* **`wts_gm_area`**: Área da sub-bacia hidrográfica em quilômetros quadrados ($km^2$).
