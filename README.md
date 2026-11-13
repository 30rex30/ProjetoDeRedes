<div align="center">

# 🌐 Projeto de Redes de Computadores

**Arquitetura, configuração e implementação de infraestrutura de rede (`ProjetoFinalRD`)**

[![Estado](https://shields.io)]()
[![Licença](https://shields.io)](LICENSE)
[![Autor](https://shields.io)](https://github.com/30rex30)

</div>

---

## 📋 Índice

1. [Sobre o Projeto](#-sobre-o-projeto)
2. [Objetivos](#-objetivos)
3. [Arquitetura e Plano de Endereçamento](#-arquitetura-e-plano-de-endereçamento)
4. [Tecnologias e Protocolos](#-tecnologias-e-protocolos)
5. [Estrutura do Repositório](#-estrutura-do-repositório)
6. [Como Executar](#-como-executar)
7. [Testes e Validação](#-testes-e-validação)
8. [Autor](#-autor)

---

## 📖 Sobre o Projeto

Este repositório reúne os ficheiros, configurações e documentação referentes ao projeto final da unidade curricular de **Redes de Computadores**, organizados no diretório **`ProjetoFinalRD`**. 

O projeto abrange o planeamento lógico e físico de uma rede corporativa/académica, garantindo segmentação de tráfego, encaminhamento eficiente, resolução de nomes, atribuição dinâmica de endereços e políticas de segurança.

---

## 🎯 Objetivos

- **Segmentação de Rede:** Isolamento de departamentos ou serviços através de VLANs e sub-redes IPv4/IPv6.
- **Encaminhamento:** Comunicação inter-VLAN e encaminhamento dinâmico/estático entre routers.
- **Serviços de Rede:** Implementação de servidores essenciais (DHCP, DNS, Web/HTTP, FTP/SSH).
- **Segurança e Controlo de Acessos:** Filtragem de tráfego com Access Control Lists (ACLs) e proteção de portas nos switches.
- **Alta Disponibilidade e Redundância:** Prevenção de loops na camada de ligação de dados e redundância de gateway *(ajustar conforme aplicado)*.

---

## 🗺️ Arquitetura e Plano de Endereçamento

> 💡 **Nota:** Atualiza a tabela abaixo com as sub-redes, VLANs e endereços exatos definidos no teu ficheiro dentro de `ProjetoFinalRD`.

| VLAN / Zona | Departamento / Função | Endereço de Rede | Máscara / Prefixo | Default Gateway |
| :--- | :--- | :--- | :--- | :--- |
| **VLAN 10** | Administração | `192.168.10.0` | `/24` (`255.255.255.0`) | `192.168.10.1` |
| **VLAN 20** | Utilizadores / Clientes | `192.168.20.0` | `/24` (`255.255.255.0`) | `192.168.20.1` |
| **VLAN 30** | Servidores (DMZ) | `192.168.30.0` | `/24` (`255.255.255.0`) | `192.168.30.1` |
| **VLAN 99** | Gestão (Management) | `192.168.99.0` | `/24` (`255.255.255.0`) | `192.168.99.1` |
| **WAN** | Ligação entre Routers | `10.0.0.0` | `/30` (`255.255.255.252`) | — |

---

## 🛠️ Tecnologias e Protocolos

- **Ambiente / Simulação:** Cisco Packet Tracer / GNS3 / Máquinas Virtuais *(manter o utilizado)*
- **Camada 2 (Switching):** Ethernet, 802.1Q (VLANs & Trunking), Spanning Tree Protocol (STP), Port Security
- **Camada 3 (Routing):** Encaminhamento Estático, OSPF / RIPv2, Router-on-a-Stick / SVI, NAT / PAT
- **Serviços de Aplicação:** DHCP, DNS, HTTP/HTTPS, SSH
- **Segurança:** Standard & Extended ACLs, encriptação de palavras-passe nos equipamentos

---

## 📁 Estrutura do Repositório

```text
ProjetoDeRedes/
├── ProjetoFinalRD/          # Ficheiros principais do projeto (topologia, configs, relatório)
│   └── ...                  # (ex: topologia.pkt, scripts/, relatorio.pdf)
└── README.md                # Documentação do repositório
```

---

## 🚀 Como Executar

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com
   ```
2. **Aceder à pasta do projeto:**
   ```bash
   cd ProjetoDeRedes/ProjetoFinalRD
   ```
3. **Abrir a topologia:**
   - Abre o ficheiro de simulação (`.pkt` ou equivalente) no **Cisco Packet Tracer** (versão recomendada: `8.2` ou superior).
   - Aguarda cerca de 30 segundos (ou utiliza o botão *Fast Forward Time*) para que todos os protocolos de convergência (STP, OSPF e DHCP) estabilizem.

---

## ✅ Testes e Validação

Para confirmar o correto funcionamento da infraestrutura implementada:

- [x] Atribuição automática de endereços IP via **DHCP** nos hosts finais.
- [x] Conectividade total entre diferentes VLANs através de testes `ping` e `tracert`.
- [x] Resolução de nomes internos e externos através do servidor **DNS**.
- [x] Bloqueio de tráfego não autorizado validado através das regras de **ACL**.
- [x] Acesso remoto seguro aos equipamentos de rede via **SSH**.

---

## 👤 Autor

Desenvolvido por **[30rex30](https://github.com/30rex30)**.

Se este projeto te foi útil, considera deixar uma ⭐ no repositório!
