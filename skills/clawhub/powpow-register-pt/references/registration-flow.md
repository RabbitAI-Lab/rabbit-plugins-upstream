# Detalhes do fluxo de registro — powpow-register

Para consulta na hora de resolver problemas. Todas as regras vêm do código-fonte da plataforma (validação
consistente frontend/backend em Next.js), com as fontes citadas. Se a plataforma for atualizada, vale o
comportamento real online.

## Pontos de entrada

- Página de registro: https://global.powpow.online/register
- Página de login: https://global.powpow.online/login
- Página de assinatura: https://global.powpow.online/subscription
- Se entrar por um link de compartilhamento com `?next=...`, após registro + pagamento o retorno é
  automático à página de origem.

## Campos do formulário e regras

| Campo | Obrigatório | Regra | Fonte no código |
|---|---|---|---|
| Avatar | Opcional | Imagem ≤5MB, sem suporte a SVG; o servidor comprime automaticamente (>100KB é comprimido para 400×400 / qualidade 90) | `src/app/api/auth/register/route.ts` |
| Nome de usuário | Obrigatório | 2~50 caracteres, após trim é armazenado em **minúsculas** (Tom e tom contam como o mesmo nome de usuário; tanto no registro quanto no login não há distinção de maiúsculas/minúsculas) | Idem (zod schema) |
| Senha | Obrigatória | 8~100 caracteres, deve conter ao mesmo tempo letra maiúscula, letra minúscula e número | Idem |
| Confirmar senha | Obrigatória | Igual à senha (validação só no frontend) | `src/app/(public)/register/page.tsx` |
| Apelido | Opcional | ≤100 caracteres; se ficar vazio, usa o nome de usuário por padrão | register route |
| E-mail | **Obrigatório** | Formato de e-mail válido, ≤255 caracteres; um e-mail só pode registrar uma conta | register route |
| Código de verificação por e-mail | **Obrigatório** | 6 dígitos; **válido por 10 minutos**; anulado assim que a validação dá certo; um reenvio marca o código antigo como usado | `src/lib/email-verification.ts` |
| Telefone | Opcional | Número da China continental, 11 dígitos começando por `1[3-9]`; um número só pode ser vinculado a uma conta | register route |

A página oferece ainda três botões de login de terceiros: **Google, Watcha, conta Huawei**
(`GoogleSignInButton` / `WatchaLoginButton` / `HuaweiLoginButton`). Contas de terceiros não têm senha
local; ao tentar login com senha depois, obtém-se
「该账号未设置密码，请使用其他方式登录」 (esta conta não tem senha definida, faça login por outro método).

## Limites de frequência e proteção anti-força bruta

| Ação | Limite | Fonte |
|---|---|---|
| Envio do registro | **3 vezes/minuto/IP**, exceder dá 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Envio do código de verificação | Mesmo IP 1 vez/minuto **e** mesmo e-mail 1 vez/minuto, exceder dá 429; o botão do frontend tem contagem regressiva de 60 segundos | `src/app/api/auth/register/send-code/route.ts` |
| Validação do código | Por e-mail, no máximo **5 tentativas** em 10 minutos; atingido o limite, rejeita mesmo com o código certo; é preciso pedir um código novo | `src/lib/email-verification.ts` |
| Envio do código «esqueci a senha» | 1 vez/minuto/IP | `src/app/api/auth/forgot-password/route.ts` |
| Login | 5 vezes/minuto/IP; a mesma conta com **5 falhas** seguidas fica **bloqueada 30 minutos** (423), com aviso de tentativas restantes decrescente durante o bloqueio | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Comportamento de proteção de privacidade**: no envio do código de verificação / «esqueci a senha», se o
e-mail já estiver registrado ou não existir, a interface devolve nos dois casos uma mensagem de sucesso
uniforme, sem revelar se o e-mail está registrado.

## Equivalência entre o modo delegado ao agent e o registro web

O script da skill chama **o mesmo conjunto de APIs públicas** (`/api/auth/register`, `send-code`, `login`,
`/api/auth/me`), e percorre exatamente as mesmas validações, limites e caminhos de erro que o envio do
formulário da página de registro — todas as regras deste arquivo se aplicam igualmente aos dois modos. A
sequência do script e o contrato de comandos estão em `references/agent-flow.md`.

## Transição de estados após um registro bem-sucedido

1. O usuário é gravado com `accountStatus: 'pending'` e **3 badges** iniciais (register route).
2. O servidor planta ao mesmo tempo dois cookies HttpOnly: o JWT (permite acessar diretamente
   `/subscription`) e o pendingUserToken (credencial de identidade do fluxo de assinatura).
3. A página de registro detecta `pending_payment` → redireciona para `/subscription` (preservando o
   parâmetro de retorno `next`); no modo delegado ao agent, usa-se `me?token=…&redirect=/subscription`
   para o mesmo efeito.
4. Pagamento concluído → `accountStatus` passa a `active` (**no Alipay a ativação é automática no servidor
   via notify**; no PayPal é automática via Webhook; no QR code WeChat é confirmação manual; no Huawei IAP
   vai por `activate-huawei`). Detalhes em `payment-and-activation.md`.

Usuários não ativados (pending) que chamem as APIs centrais (feed, mapa, conversa com humanos digitais,
check-in etc.) recebem sempre 403; exceto os links de posts compartilhados (que permanecem de acesso
público).

## Tabela de diagnóstico de erros comuns

| Sintoma | Causa | O que fazer |
|---|---|---|
| 「用户名已存在」 (o nome de usuário já existe) | Nome de usuário ocupado (sem distinção de maiúsculas/minúsculas) | Usar outro nome de usuário |
| 「邮箱已被使用」 (o e-mail já está em uso) | O e-mail já foi registrado antes | Trocar de e-mail; ou ir por login +「忘记密码」(esqueci a senha) para recuperar a conta antiga |
| 「邮箱验证码错误或已过期」 (código de verificação errado ou expirado) | Código digitado errado / passou de 10 minutos / rejeitado por mais de 5 tentativas | Clicar em 「重新发送」(reenviar) e usar o código do **e-mail mais recente** |
| Não chega o código de verificação | Limite de 60 segundos; ou caiu no spam / e-mails promocionais | Esperar acabar a contagem regressiva e reenviar; vasculhar a pasta de spam |
| 「手机号已被使用」 (o telefone já está em uso) | O número já está vinculado a outra conta | Remover o telefone (é opcional) ou trocar de número |
| 「注册请求过于频繁」 (solicitação de registro frequente demais) / 429 | Teto de 3 registros/minuto/IP atingido | Esperar alguns minutos e tentar de novo |
| 409 「用户名或邮箱已被注册」 (nome de usuário ou e-mail já registrado) | Colisão com outra pessoa no instante do envio (rede de segurança contra concorrência) | Trocar nome de usuário ou e-mail e tentar de novo |
| 「图片大小不能超过5MB」 (a imagem não pode passar de 5MB) / 「不支持 SVG」 (SVG não suportado) | Avatar fora da norma | Trocar de imagem ou pular o avatar |
| Registro bem-sucedido mas login 403 「请完成订阅以激活账户」 (conclua a assinatura para ativar a conta) | A conta continua pending (estado esperado antes do pagamento) | Antes de pagar: é normal, conclua primeiro a assinatura; 403 depois de pagar: foi usado um JWT antigo; no modo script, rode primeiro `refresh-login` para renovar o estado de sessão |
| Login 423 「账户已锁定」 (conta bloqueada) | 5 erros seguidos de senha | Esperar 30 minutos |
| Login 401 「还剩 N 次尝试机会」 (restam N tentativas) | Senha errada, perto do bloqueio | Pensar bem antes de tentar, ou ir direto por 「忘记密码」(esqueci a senha) |
| 「该账号未设置密码，请使用其他方式登录」 (esta conta não tem senha definida, faça login por outro método) | Conta de terceiros (Google/Watcha/Huawei) | Fazer login com o botão de terceiros original |
| 「该账号已注销」 (esta conta foi cancelada) | A conta foi desativada | É preciso registrar-se de novo |

## Saber mais sobre login (útil de passagem para diagnóstico)

O login aceita entrada tripla **nome de usuário / e-mail / telefone** (qualquer um dos três serve como
identificador da conta). Esqueci a senha: página de login → 「忘记密码」(esqueci a senha) → digitar o
e-mail de registro para receber um código de 6 dígitos → redefinir.
