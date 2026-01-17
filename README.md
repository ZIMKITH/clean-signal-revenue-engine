# The Clean-Signal Revenue Engine

![n8n](https://img.shields.io/badge/Orchestration-n8n-red?style=for-the-badge&logo=n8n)
![JavaScript](https://img.shields.io/badge/Code-JavaScript-yellow?style=for-the-badge&logo=javascript)
![Governance](https://img.shields.io/badge/Impact-Revenue_Protection-green?style=for-the-badge)

**Stop burning leads. Start engineering revenue.**
A deterministic GTM pipeline that guarantees 100% data hygiene before it hits your CRM.

## The Problem
In modern GTM stacks (Clay, Instantly, Salesforce), **speed kills**. 
Automated enrichment tools often inject "dirty" data—such as legal entity suffixes, incorrect formatting, or high-risk companies (including bankruptcies/fraud)- directly into outreach sequences.
**Result:** Damaged Domain Reputation (SPF/DKIM), wasted SDR time, and lost revenue.

## The Solution: "Glass Box" Architecture
This repository hosts a production-ready **Governance Firewall**. It intercepts raw leads and forces them through a strict hygiene protocol using **Raw JavaScript** and **n8n**. 

**It is not an AI wrapper. It is a deterministic logic gate.**

## Architecture Flow

```mermaid
graph TD
    A[Webhook Ingestion] -->|Raw Data| B(The Laundromat<br/><i>Code Node</i>)
    B -->|Normalized Data| C{The Gatekeeper<br/><i>Logic Gate</i>}
    C -->|PASS| D[HTTP Request<br/><i>CRM/API</i>]
    C -->|FAIL| E[Quarantine Log<br/><i>Google Sheets</i>]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#fff,stroke:#d00,stroke-width:4px
    style D fill:#9f9,stroke:#333,stroke-width:2px
    style E fill:#faa,stroke:#333,stroke-width:2px
