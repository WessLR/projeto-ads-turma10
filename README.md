# 📢 Sistema de Ouvidoria — Turma 10

Sistema de gerenciamento de reclamações via terminal, desenvolvido em Python com integração ao banco de dados MySQL. Projeto acadêmico do curso de ADS (Análise e Desenvolvimento de Sistemas) — Turma 10.

---

## 📋 Funcionalidades

- ✅ Registrar nova reclamação
- 📄 Listar todas as reclamações cadastradas
- 🔍 Pesquisar reclamação por código
- ✏️ Atualizar descrição de uma reclamação
- 🗑️ Remover uma reclamação

---

## 🗂️ Estrutura do Projeto

```
projeto-ads-turma10/
│
├── Ouvidoria.py        # Lógica principal do sistema (menus e operações)
├── operacoesbd.py      # Módulo de conexão e operações com o banco de dados
└── sub categorias      # Arquivo auxiliar de subcategorias
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **MySQL** — banco de dados relacional
- **mysql-connector-python** — biblioteca de conexão Python ↔ MySQL

---

## ⚙️ Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.x
- MySQL Server
- Biblioteca `mysql-connector-python`

Para instalar a biblioteca:

```bash
pip install mysql-connector-python
```

---

## 🗄️ Configuração do Banco de Dados

Crie o banco de dados e a tabela no MySQL:

```sql
CREATE DATABASE Ouvidoria;

USE Ouvidoria;

CREATE TABLE Ouvidoria (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    categoria VARCHAR(100) NOT NULL
);
```

---

## 🔧 Configuração da Conexão

No arquivo `Ouvidoria.py`, ajuste as credenciais de conexão conforme seu ambiente:

```python
conexao = criarConexao('localhost', 'seu_usuario', 'sua_senha', 'Ouvidoria')
```

---

## ▶️ Como Executar

```bash
python Ouvidoria.py
```

---

## 📦 Módulo `operacoesbd.py`

Módulo responsável por toda a comunicação com o banco de dados. Expõe as seguintes funções:

| Função | Descrição |
|---|---|
| `criarConexao()` | Estabelece a conexão com o MySQL |
| `encerrarConexao()` | Encerra a conexão com o banco |
| `insertNoBancoDados()` | Insere um novo registro |
| `listarBancoDados()` | Retorna registros do banco |
| `atualizarBancoDados()` | Atualiza um registro existente |
| `excluirBancoDados()` | Remove um registro do banco |

Todas as funções utilizam **prepared statements** e **tratamento de exceções**, com rollback automático em caso de erro.

---

## 👥 Autores

Desenvolvido pela **Turma 10** — ADS

---

## 📄 Licença

Este projeto é de uso acadêmico.
