# powpow-register

O assistente de registro da Bubble da PowPow (edição OpenClaw): leva um novo usuário de « não sei o que é a Bubble » a « conta ativada e pronta para usar » — apresentação do produto (com capturas de tela da interface), guia passo a passo de registro, solução de erros e explicação da ativação da assinatura.

Skill puramente orientativo, sem scripts nem dependências; todas as ações de registro são feitas pelo usuário no navegador/Aplicativo.

## Instalação

```
openclaw skills install @durenzidu/powpow-register
```

## Recursos

1. **Apresentação do produto**: introdução de ~120 caracteres + links de capturas hospedadas em um repositório público do GitHub (6 imagens: página de mapa, página de detalhes do post, etc.; envie 1–3 conforme o cenário).
2. **Guia de registro**: regras dos campos (nome de usuário/senha/código de verificação de e-mail/telefone/avatar), login de terceiros (Google/Watcha/Huawei), parâmetros de limite de frequência — tudo extraído do código-fonte da plataforma, com fontes citadas.
3. **Solução de erros**: 13 problemas comuns, incluindo código de verificação não recebido, nome de usuário/e-mail já em uso, 403 não ativado, conta bloqueada.
4. **Ativação da assinatura**: três canais — PayPal (web) / QR code WeChat (confirmação manual) / IAP Huawei (HarmonyOS) — com explicações e solução de erros; a cadeia de pagamento existente é reutilizada como está, o skill apenas mostra o caminho.

## Estrutura de arquivos

```
powpow-register/
├── SKILL.md                            # Guia principal (acionadores, fluxo, regras de tom)
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # Regras de campos, limites, tabela de erros (com fontes)
    ├── payment-and-activation.md       # Ativação de assinatura, canais de pagamento, conclusão de reutilização
    └── screenshots.md                  # Lista de capturas hospedadas + consulta rápida por cenário
```

## Segurança

- Não contém segredos; sem scripts, nunca toca nas credenciais do usuário.
- **Nunca peça** a senha, o código de verificação ou os comprovantes de pagamento do usuário; o registro e o pagamento acontecem inteiramente nas páginas da plataforma.

## Licença

MIT-0 (licença unificada do ClawHub).

## Links

- Site oficial: https://global.powpow.online
- Registro: https://global.powpow.online/register
- Conhecer a Bubble (vídeo): https://www.bilibili.com/video/BV1Wu826UEVz/