# Fluxo de gestão delegada do agent e contrato do script — powpow-register

Detalhes de execução de cada etapa do SKILL.md. Todos os comandos são `node scripts/powpow-register.mjs <subcomando> [parâmetros]`,
o script é **zero dependências** e requer **Node ≥ 18**; todas as requisições vão apenas para `https://global.powpow.online`.

## Design de segurança (por que é assim)

| Design | Razão |
|---|---|
| A senha só entra pela variável de ambiente `POWPOW_REGISTER_PASSWORD` | Os argumentos de linha de comando de um processo ficam visíveis para os demais processos da mesma máquina (superfície de vazamento do argv); a variável de ambiente é lida dentro do script e usada na hora |
| A senha **jamais é escrita no arquivo de estado**, jamais aparece nos logs | O arquivo de estado pode permanecer no disco; no modo geração ela só é exibida uma vez para o usuário salvar |
| O arquivo de estado fica no diretório temporário do sistema (`os.tmpdir()/powpow-register-state.json`, 0600) | Contém apenas os cinco campos email / username / nickname / token / outTradeNo; o `cleanup` apaga tudo de uma vez |
| O JWT que o agent recebe é trocado por um cookie de navegador pelo endpoint oficial `me?token=` | É a ponte oficial desenhada pela plataforma para o WebView do HarmonyOS; a verificação confere só assinatura + validade, sem amarrar à impressão digital do aparelho, logo o navegador do usuário serve |
| O pagamento só faz create-order / query / abrir o caixa | O ato de pagar e as credenciais de pagamento ficam sempre entre o usuário e o caixa oficial do Alipay; o agent não pega neles |

## Referência de comandos

| Comando | Parâmetros-chave | O que faz / quando |
|---|---|---|
| `status` | —— | Ver o progresso do fluxo (lê o arquivo de estado); depois de uma conversa interrompida, rode isto primeiro |
| `gen-password` | —— | Gera uma senha forte de 24 caracteres (maiúsculas + minúsculas + números); o stdout exibe **só esta uma vez** |
| `prepare-suggest` | `--username --nickname --email` | Anota no arquivo de estado as informações confirmadas (depois o register não pede de novo) |
| `send-code` | `--email` | Dispara o envio pela plataforma do código de verificação de 6 dígitos (válido 10 minutos, espera de 60s) |
| `register` | `--code` (obrigatório); `--username --nickname --avatar --phone` (opcionais, dispensados se já estão no arquivo de estado) | Cria a conta pending; a senha vai pela variável de ambiente `POWPOW_REGISTER_PASSWORD`; após o sucesso o JWT é guardado automaticamente no arquivo de estado |
| `login-link` | `--target pending` ou `--target home` | Gera um link de login com um clique (design de link duplo, veja abaixo) |
| `create-order` | `--package monthly\|quarterly\|yearly` | Cria o pedido no Alipay; devolve o caminho do arquivo da página de pagamento + outTradeNo (anotado automaticamente no arquivo de estado) |
| `query` | —— | Consulta o estado do pedido `paid / pending / closed / unknown` (o outTradeNo vem do arquivo de estado), consulta a cada 10–15s |
| `refresh-login` | Senha por variável de ambiente | Faz login de novo e troca por um **JWT novo** (a declaração de assinatura passa de NONE para ACTIVE); obrigatório depois que o pagamento cai |
| `whoami` | —— | Consulta com o token do arquivo de estado o estado da conta e da assinatura (verificar se a ativação valeu) |
| `cleanup` | —— | Apaga o arquivo de estado (obrigatório no encerramento) |

**Passagem da variável de ambiente** (a senha jamais vai para a linha de comando):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<senha>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<senha>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<senha> && node scripts/powpow-register.mjs register --code 123456
```

## Mecanismo de link duplo (design central)

O estado de sessão da plataforma é um cookie HttpOnly, e o agent não pode plantar diretamente um cookie no navegador; a ponte é o endpoint oficial
`/api/auth/me?token=<JWT>&redirect=<caminho interno do site>`: verificação de assinatura → para o usuário pending é criada automaticamente uma
session → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 dias) → validação do
redirect (só caminho começando com uma única barra, proibidos `//` e a barra invertida, e após resolução tem de ser da mesma origem) → 307 redirecionamento temporário para a página de destino.

- **Link 1 (entregar imediatamente após o registro bem-sucedido)**: `--target pending` → cai em `/subscription`.
  O navegador do usuário entra em estado de «semi-sessão»: a página de assinatura e a de retorno do Alipay ficam visíveis e operáveis; as páginas de conteúdo continuam barradas de volta para a de
  assinatura (tripla proteção: checagem dos claims do JWT no gateway → re-checagem no BD → checagem nas APIs centrais; é comportamento normal).
- **Link 2 (entregar depois de confirmar o paid)**: primeiro `refresh-login` para trocar por um JWT novo (o pagamento só atualiza o BD, não altera os
  claims de um JWT já emitido; sem a troca, manifesta-se como «paguei mas não tenho membro»), depois `--target home` → cai na home,
  com o estado de membro completo.

## Sequência completa (caminho normal)

```
1.  status                          # autoverificação do ambiente
2.  (a etapa 2 é confirmar dados na conversa, senha com duas opções; modo geração: gen-password → o usuário salva imediatamente)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → o usuário vai ao e-mail ver o código (única saída da conversa, momento ①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → link 1 enviado ao usuário
7.  (o usuário escolhe o plano) create-order --package monthly
8.  start <arquivo da página de pagamento>   # Windows; no macOS usar open, no Linux xdg-open
     # → o usuário paga no caixa do Alipay (saída da conversa, momento ②)
9.  query (a cada 10–15s) até paid
10. refresh-login                   # troca pelo JWT novo com declaração ACTIVE
11. login-link --target home        # → link 2 enviado ao usuário
12. whoami                          # confirmar subscriptionStatus: ACTIVE (opcional)
13. cleanup                         # limpar o arquivo de estado
```

## Mapeamento comando → API da plataforma

| Comando do script | Interface da plataforma |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, upload direto do avatar) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (o link em si, vale ao ser clicado no navegador) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

Origem das regras: campos de registro e limites de frequência em `registration-flow.md`; planos e cadeia de ativação em
`payment-and-activation.md` (ambos citam os arquivos do código-fonte da plataforma).

## Tratamento de erros a nível de script

| Sintoma | Tratamento |
|---|---|
| `Versão do Node baixa demais` | Recue para o modo de orientação pura, não force |
| Erro de rede / timeout | Tente uma vez de novo; se continuar falhando, o usuário verifica a rede e segue (o arquivo de estado continua lá; recupere rodando `status` desde o início) |
| register devolve erro de negócio (nome de usuário já existe etc.) | Trate pela tabela da etapa 5 do SKILL.md, **não é preciso reenviar o código de verificação** (continua válido por 10 minutos) |
| register devolve 「邮箱验证码错误或已过期」 (código de verificação errado ou expirado) | Tempo esgotado → rodar `send-code` de novo |
| O usuário fechou a página de pagamento depois do `create-order` | Rode `create-order` de novo direto (o pedido antigo fecha sozinho em 2h) |
| `query` fica em pending | O usuário talvez não tenha pago; pergunte. Se pagou mesmo → siga a tabela de diagnóstico do payment-and-activation.md |
| `refresh-login` dá 403 `pending_payment` | O pagamento ainda não caiu; volte à etapa 9 e continue consultando |
| Arquivo de estado perdido (apagado sem querer / troca de máquina) | `whoami`/`refresh-login` ficam inutilizáveis; o usuário atualiza direto a página de assinatura no navegador onde abriu o link 1 para confirmar o estado, ou faz login de novo (modo web) |

## Modo de recuo (orientação pura)

Em qualquer destas situações, recue imediatamente para a orientação pura estilo v1 e pare de insistir com o script:

- Não há Node ≥ 18, ou o script falha duas vezes seguidas na mesma coisa;
- O usuário diz claramente «eu mesmo faço na página web»;
- Políticas da empresa / do aparelho restringem scripts de rede.

Depois do recuo: entregue a página de registro https://global.powpow.online/register e a de assinatura
https://global.powpow.online/subscription, acompanhe na resolução de erros pelas regras de
`registration-flow.md`, mantenha o tom e feche cada rodada com o bloco de «próximo passo».
