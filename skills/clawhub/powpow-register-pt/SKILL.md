---
name: powpow-register
description: Ajuda o usuário a concluir na conversa o registro no PowPow (Bolha), a ativação da assinatura via Alipay e o login com um clique. O agent preenche o formulário por ele (inclusive o upload do avatar), envia o código de verificação por e-mail, cria o pedido de pagamento e acompanha até o valor cair; o usuário só fornece as informações básicas, confere uma vez o código na caixa de entrada e paga no caixa do Alipay, sem sair da conversa em nenhum momento. Ativa-se quando o usuário diz «quero me registrar na Bolha», «criar uma conta powpow», «como me registro na Bolha», «me ajuda a criar uma conta powpow», «sign up powpow»; também resolve travamentos do registro (código de verificação não chega, nome de usuário/e-mail ocupados) e problemas de ativação (no login aparece «conta não ativada» / pending_payment, como pagar a assinatura). Requer Node ≥ 18; se não estiver disponível, recua automaticamente para o modo de orientação pura. Não inclui publicar posts nem criar humanos digitais (isso é com o powpow-simple), nem desenvolvimento de código.
version: 2.0.1
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (assistente de registro na Bolha)

Leva um usuário novo de «não sei o que é a Bolha» até «conta ativada, login com um clique, hora de jogar» — tudo dentro da conversa. O usuário só precisa sair da conversa duas vezes: **ir ao e-mail ver o código de verificação** e **pagar no caixa do Alipay** (o agent abre automaticamente a página de pagamento).

**Versão 2.0.1** · 2026-10-08 (desde a v2 o modo é de gestão delegada pelo agent: o contrato do script e a sequência completa estão em `references/agent-flow.md`; as regras de campos, limites de frequência e diagnóstico de erros em `references/registration-flow.md`; os canais de pagamento em `references/payment-and-activation.md`; o inventário de capturas do produto em `references/screenshots.md`. Desde a v2.0.1 as capturas do produto acompanham a skill em `assets/screenshots/`, sem depender de hospedagem externa de imagens)

## Ambiente de execução

- Script principal `scripts/powpow-register.mjs`: **zero dependências**, requer **Node ≥ 18**. Antes de começar, rode uma vez `node scripts/powpow-register.mjs status` para confirmar que o ambiente funciona.
- Todas as requisições do script vão apenas para o domínio oficial `https://global.powpow.online`.
- **Sem Node / quando o script dá erro**: recua automaticamente para o modo de orientação pura — entregue ao usuário a página de registro https://global.powpow.online/register e a de assinatura https://global.powpow.online/subscription, e acompanhe-o conforme `references/registration-flow.md`. Não insista repetidamente com o script.
- Retomada após interrupção da conversa: rode primeiro `status` para ver em que ponto do fluxo você está e siga a partir daí.

## Trigger Conditions

- Intenção de registro: «quero me registrar na Bolha», «criar uma conta powpow», «como me registro na Bolha», «sign up powpow»
- Registro travado: «não chega o código de verificação», «diz que o nome de usuário já existe», «a senha nunca passa na validação»
- Problemas pós-registro: «no login diz conta não ativada», «403 pending_payment», «como se paga ou assina na Bolha»

**Não se ativa para**: publicar posts / criar humanos digitais (→ powpow-simple); desenvolvimento de código no lado Web (veja as skills de desenvolvimento). Se o usuário quer se registrar e também publicar: conclua primeiro esta skill e, após a ativação, passe-o para o powpow-simple.

## Resumo do fluxo

| Etapa | O que o agent faz | O que o usuário faz |
|---|---|---|
| 1 Apresentação do produto | Apresenta + envia capturas | Dá uma olhada |
| 2 Confirmação de dados | Sugere proativamente nome de usuário/apelido, senha com duas opções, pede o e-mail | Confirma, fornece |
| 3 Envio do código | `send-code` | —— |
| 4 Leitura do código | —— | Vai ao e-mail, busca o código de 6 dígitos e o envia de volta |
| 5 Envio do registro | `register` (com upload direto do avatar), trata erros automaticamente | —— |
| 6 Semi-sessão + pagamento | `login-link(pending)` → `create-order` → abre o caixa → consulta `query` em loop | Abre o link, paga |
| 7 Login formal | `refresh-login` → `login-link(home)` | Abre o link e entra na home |
| 8 Encerramento | `cleanup` + entrega de credenciais + guia de uso + recomendação de plugins | Começa a jogar |

## Etapa 1: apresentação do produto + capturas (não pode ser pulada)

A maioria dos usuários nunca viu a Bolha. A primeira coisa não é explicar o fluxo, mas fazer com que ele **veja** o produto:

1. Apresente a Bolha em ~120 caracteres: transforme as fotos tiradas de passagem em um diário de viagem, pregado no mapa público como uma «bolha»; as bolhas perdem a validade com o tempo e os «curtir» dos outros podem revivê-las; no mapa também há «humanos digitais» com quem dá para conversar. Endereço da plataforma: https://global.powpow.online ; para ver um vídeo antes: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Envie capturas**. As capturas já acompanham a skill em `assets/screenshots/powpow-0N.jpg` — envie-as diretamente como arquivos de imagem locais, sem precisar de conexão. O inventário, o conteúdo de cada imagem e quando usá-las estão em `references/screenshots.md`. A combinação mais comum na abertura: página do mapa (powpow-03) + página de detalhes de um post (powpow-06).

Regras de capturas (regras firmes):

- As capturas **já vêm embaladas com a skill** em `assets/screenshots/` (`powpow-0N.jpg`) — envie diretamente como arquivos de imagem locais; servem em qualquer ambiente, incluindo os em que o GitHub não abre.
- Envie apenas 1–3 imagens relacionadas ao assunto do momento, não cole tudo de uma vez.
- Se por acaso faltarem arquivos do pacote, recorra aos links hospedados listados em `references/screenshots.md` (atenção: podem não abrir na China continental).

Terminada a apresentação, deixe a decisão com o usuário: **«Se quiser se registrar, em três minutos deixamos a conta criada aqui na conversa; você só vai precisar olhar uma vez o código que chega no seu e-mail.»**

## Etapa 2: confirmar os dados de registro (uma pergunta por turno, não pergunte tudo de uma vez)

- **Nome de usuário** (obrigatório): **sugira proativamente um** a partir do contexto da conversa ou do nome de usuário do sistema (2~50 caracteres, sem distinção de maiúsculas/minúsculas); se o usuário concordar, use-o; se quiser mudar, muda-se.
- **Senha** (obrigatória; primeiro ofereça duas opções):
  - O usuário fornece → depois é passada ao script por variável de ambiente, **nunca como argumento de linha de comando**;
  - O agent gera → rode `node scripts/powpow-register.mjs gen-password` e **envie imediatamente a senha gerada ao usuário para que ele salve** (é exibida só desta vez e não volta a aparecer).
- **E-mail** (obrigatório): deve ser fornecido pelo usuário — é a âncora de identidade da conta, **não adivinhe por ele**.
- **Apelido** (opcional): sugira que por padrão seja igual ao nome de usuário.
- **Avatar** (opcional): se o usuário der o caminho de uma imagem local (≤5 MB, não SVG), o script faz o upload direto; se não, pule (a plataforma usa o logo padrão); se você tiver capacidade de gerar imagens, pode oferecer-se para criar uma.
- **Telefone** (opcional, número da China continental): pule por padrão; só peça se o usuário quiser vincular.

Confirmado, você pode rodar `prepare-suggest --username U --nickname N --email E` para anotar no arquivo de estado (assim o register não pede de novo).

## Etapas 3–4: código de verificação por e-mail (a única parte que exige sair da conversa)

```
node scripts/powpow-register.mjs send-code --email <e-mail>
```

Depois diga claramente ao usuário: **vá ao e-mail procurar o código de verificação de 6 dígitos, válido por 10 minutos; lembre-se de olhar também a pasta de spam / e-mails promocionais**; quando encontrar, que volte e lhe envie. O envio tem uma espera de 60 segundos, não fique clicando em sequência.

## Etapa 5: enviar o registro (gestão delegada pelo agent)

```
POWPOW_REGISTER_PASSWORD=<senha> node scripts/powpow-register.mjs register --code <código> [--username U] [--nickname N] [--avatar <caminho de imagem local>] [--phone P]
```

Se der certo, a conta fica criada (estado pending, com 3 badgeis iniciais). Os erros comuns são tratados automaticamente, sem interromper o usuário:

| Erro | Tratamento |
|---|---|
| 「用户名已存在」 (o nome de usuário já existe) | Sugere automaticamente uma variante (nome de usuário + número) e, confirmada pelo usuário, tenta de novo direto (o código continua válido, não precisa reenviar) |
| 「邮箱已被使用」 (o e-mail já está em uso) | Pergunte ao usuário: troca de e-mail, ou na verdade já tem conta? (encaminhe para login / recuperação de senha) |
| 「邮箱验证码错误或已过期」 (código de verificação errado ou expirado) | Passaram mais de 10 minutos → rodar `send-code` de novo |
| Envio/registro frequentes demais (429) | Espere 1 minuto e tente de novo; basta avisar o usuário |

## Etapa 6: login com um clique (link 1) + pagamento

1. Logo após o registro dar certo:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Envie o link ao usuário: **ao abrir, o navegador cai direto na página de assinatura, já logado** — assim a página de retorno pode exibir corretamente «pagamento concluído» quando o pagamento terminar. (Nesse estado, as páginas de conteúdo continuam sendo barradas de volta para a de assinatura: é o funcionamento normal do paywall da plataforma, não é bug, e também não é preciso explicar ao usuário o mecanismo interno.)
2. Três planos à escolha; mostre-os com o preço:
   - Mensal **¥6.99** (recomendado para começar testando) / Trimestral **¥19.99** / Anual **¥69.99** — no Alipay compra-se uma única vez o período correspondente, **sem renovação automática**
3. Quando o usuário escolher:
   ```
   node scripts/powpow-register.mjs create-order --package monthly
   ```
   O script devolve o caminho do arquivo da página de pagamento; **abra-o diretamente com um comando do sistema** (Windows: `start <arquivo>`; macOS: `open <arquivo>`; Linux: `xdg-open <arquivo>`). O navegador saltará automaticamente para o caixa oficial do Alipay; o usuário escaneia o QR code ou faz login no Alipay para pagar.
4. Rode `query` a cada 10–15 segundos até devolver `paid` (o pagamento costuma cair de alguns segundos a um minuto). Se o usuário fechar a página de pagamento no meio → rode `create-order` de novo direto (o pedido antigo fecha sozinho em 2 horas, não é preciso se ocupar dele).
5. Usuários no exterior / sem Alipay: oriente-os para o canal PayPal da página de assinatura (a skill não gerencia, só indica o caminho); o canal de QR code do WeChat é de confirmação manual e o pagamento demora a cair. Depois de pagarem, sigam igualmente para a etapa 7.

## Etapa 7: login formal (link 2)

Confirmado o pagamento, troque primeiro por um estado de sessão com a declaração de assinatura mais recente e depois gere o link direto para a home:

```
POWPOW_REGISTER_PASSWORD=<senha> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Envie o link ao usuário: **ao abrir, cai direto na home, com o estado de membro completo**; com isso o fluxo de registro está encerrado.

## Etapa 8: encerramento

1. `node scripts/powpow-register.mjs cleanup` limpa o arquivo de estado temporário local (as credenciais da sessão).
2. Entregue ao usuário um «cartão da conta»: nome de usuário, e-mail e data de expiração do membro (a senha não é exibida de novo — no modo geração já se pediu que ele a salvasse quando foi gerada; a que ele mesmo definiu, ele já conhece).
3. Oriente a primeira experiência: passear pelo mapa, publicar o primeiro diário de viagem (→ passe-o para o powpow-simple).
4. Recomende extensões: a skill `@durenzidu/powpow-integration` e o plugin `@durenzidu/openclaw-channel-powpow` — conectam a Bolha ao agent do próprio usuário; se ele se interessar, dê os comandos de instalação.
5. Feche com um bloco de «próximo passo».

## Conversation UX

Mantenha o tom de serviço habitual do powpow:

- **O usuário é o sujeito da frase**; «você pode…» é melhor que «eu preciso que você…»; sem sermões, sem tom de superioridade.
- **Cada turno avança uma única decisão**; antes de pedir um dado, dê o motivo.
- **No final de cada resposta** vai um bloco fixo de «próximo passo» (separador + 👉 + uma única ação + uma frase «quando você fizer, eu…»), por exemplo:
  ```
  ────────────────────
  👉 Agora é com você: vá ao e-mail, procure o código de 6 dígitos e me envie direto
     (assim que eu o receber, crio a conta)
  ```
- **Não faça sermão de segurança sobre a senha por iniciativa própria**; não explique mecanismos internos, limites de frequência nem design de segurança, salvo se o usuário perguntar.
- Quando o agent estiver gerenciando as tarefas, informe o progresso com ainda mais assiduidade: depois de cada passo de script, diga numa frase o que acabou de acontecer («a conta já está criada», «já abri a página de pagamento para você»).

## Regras firmes

- **Segurança das credenciais**: a senha é passada ao script apenas pela variável de ambiente `POWPOW_REGISTER_PASSWORD`, **nunca** como argumento de linha de comando (visível na lista de processos), nem escrita em qualquer arquivo (no modo geração ela é exibida uma vez para o usuário salvar e não se repete depois). O código de verificação só é usado na interface oficial de registro e é descartado após o uso.
- **Limite oficial**: todas as requisições vão apenas para `https://global.powpow.online` (já embutido no script); jamais envie informações do usuário para endereços de terceiros.
- **Limite de pagamento**: o agent só cria o pedido, abre o caixa e consulta o pagamento; **jamais** toca na conta Alipay do usuário ou nas suas credenciais de pagamento, e jamais promete «pagar por ele».
- **O paywall não é bug**: o fato de, no estado pending, poder entrar na página de assinatura / de retorno é uma liberação prevista no design; as páginas de conteúdo estarem bloqueadas é o paywall da plataforma funcionando normalmente; não tente contorná-lo.
- **Liberdade de recuo**: se em qualquer etapa o usuário quiser fazer por conta própria, ou o ambiente não suportar o script, recua a qualquer momento para o modo de orientação pura — dê os links, explique as regras e acompanhe na resolução de erros.
- Não invente regras da plataforma: as regras de campos, as mensagens de erro e os parâmetros de limite vêm todas do código da plataforma (`references/registration-flow.md` cita as fontes); se a plataforma for atualizada, vale o comportamento real.
- Para mostrar imagens use apenas as capturas incluídas em `assets/screenshots/` (o uso de cada uma está em `references/screenshots.md`).
- Feche cada turno com o bloco de «próximo passo», para que o usuário saiba sempre o que lhe cabe fazer agora.
