# Ativação de assinatura e pagamento — powpow-register

## Conclusão (primeiro a resposta)

**Os métodos de pagamento existentes são diretamente reutilizáveis — o skill assistente de registro não exige nenhum desenvolvimento de pagamento.**

Motivos:

1. A interface de registro (`src/app/api/auth/register/route.ts`) já emite um cookie JWT + um cookie HttpOnly pendingUserToken ao criar a conta pending, então quando o usuário chega em `/subscription` já está com a sessão iniciada — os três canais de pagamento dependem dessa página de assinatura e todos ativam a mesma conta pending.
2. A interface de login retorna 403 + `redirectTo: '/subscription'` para contas pending e define os cookies da mesma forma — um usuário que pague depois sempre será levado de volta à mesma página.
3. Portanto, o limite de responsabilidade de um skill de orientação de registro é simplesmente « levar o usuário até /subscription »; não é preciso nova interface de pagamento, nem novo modelo de pedido, nem mudanças no backend.

Também é importante: a etapa de pagamento (botão do SDK JS do PayPal, confirmação manual do QR code WeChat, IAP nativo da Huawei) **torna impossível e inadequado que um skill de linha de comando/chat pague pelo usuário**. Não tente chamar interfaces de pagamento por script para pagar no lugar dele, nem peça os comprovantes de pagamento do usuário.

## Os três canais da página de assinatura

A página de assinatura `src/app/(public)/subscription/page.tsx` mostra automaticamente o canal adequado conforme o ambiente de execução:

| Canal | Ambiente | Mecanismo | Ativação |
|---|---|---|---|
| Assinatura PayPal | Web (fora do HarmonyOS) | `/api/subscription/create` cria uma assinatura PayPal → redireciona para a autorização do PayPal; renovação automática mensal, cancelável a qualquer momento (`/api/subscription/manage`) | O Webhook do PayPal (`BILLING.SUBSCRIPTION.*`) define `accountStatus` como active automaticamente |
| Assinatura por QR code WeChat | Web (fora do HarmonyOS) | Seção « Assine escaneando o WeChat » no rodapé da página: transferência escaneando o código, **ativação após confirmação manual** (`WechatQrPaymentSection`) | Confirmação manual; o crédito pode demorar — não conclua rápido que falhou logo após o pagamento |
| Compra integrada Huawei (IAP) | Dentro do App HarmonyOS | Na WebView do HarmonyOS, PayPal/WeChat Pay não estão disponíveis; a página usa o nativo `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` verifica o pedido da Huawei e então ativa |

Os planos e preços são lidos dinamicamente de `/api/subscription/plans` (planos PayPal); o texto fixo da página: Auto-renews. Cancel anytime.

## Status e redirecionamentos

- Pagamento bem-sucedido → `/subscription/success` (o callback do PayPal traz `subscriptionId`) → conta active → retorno automático à página original indicada pelo parâmetro `next` (início se não houver).
- Um usuário já assinante que visita a página de assinatura → mostra "You're All Set!", volta ao início após 3 segundos.
- Falha/cancelamento do pagamento → `/subscription/cancel`, é possível tentar novamente.

## Solução de problemas

| Mensagem | Tratamento |
|---|---|
| Ainda 403 depois de pagar | PayPal: o Webhook às vezes atrasa — faça logout e login para atualizar o status (o login reconsulta o último status no banco); WeChat: a confirmação manual ainda não terminou, aguarde um pouco; Huawei: verifique se a página de sucesso do pagamento integrado apareceu |
| A página de assinatura mostra "No subscription plans available" | Não há planos PayPal utilizáveis em `/api/subscription/plans` — um problema de configuração do lado da plataforma; peça ao usuário para tentar mais tarde |
| Pagou via WeChat mas não foi ativado | A confirmação manual é assíncrona; se em algumas horas não ativar, contate o suporte da plataforma (dongtao@outlook.com) |

## Observação: Alipay

No código existe um conjunto de pagamentos web Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`, um modelo de compra única: assinatura normal ¥9,90 / assinatura premium ¥99; degrada automaticamente para pagamento simulado se a chave do sandbox não estiver configurada), **mas não está conectado à UI da página de assinatura** — é código ocioso/em reserva. Se no futuro o Alipay precisar ser habilitado na página de assinatura, basta conectar esse código já pronto — isso não tem relação com este skill e é anotado apenas como referência para decisões do lado da plataforma.