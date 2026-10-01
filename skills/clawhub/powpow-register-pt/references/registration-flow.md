# Fluxo de registro em detalhe — powpow-register

Referência para solução de problemas. Todas as regras vêm do código-fonte da plataforma (validação consistente do Next.js no frontend e no backend), com as fontes citadas.
Quando a plataforma for atualizada, vale o comportamento real online.

## Pontos de entrada

- Página de registro: https://global.powpow.online/register
- Página de login: https://global.powpow.online/login
- Página de assinatura: https://global.powpow.online/subscription
- Quem chega por um link compartilhado com `?next=...`, após o registro + pagamento, é levado automaticamente de volta à página original.

## Campos do formulário e regras

| Campo | Obrigatório | Regra | Fonte |
|---|---|---|---|
| Avatar | Opcional | Imagem ≤5MB, SVG não suportado; compressão automática no servidor (>100KB é comprimida para 400×400 / qualidade 90) | `src/app/api/auth/register/route.ts` |
| Nome de usuário | Obrigatório | 2–50 caracteres, salvo em **minúsculas** após o trim (Tom e tom são tratados como o mesmo nome de usuário; registro e login não diferenciam maiúsculas) | idem (esquema zod) |
| Senha | Obrigatório | 8–100 caracteres, deve conter letras maiúsculas, letras minúsculas e números | idem |
| Confirmar senha | Obrigatório | Deve coincidir com a senha (validação apenas no frontend) | `src/app/(public)/register/page.tsx` |
| Apelido | Opcional | ≤100 caracteres; se vazio, usa o nome de usuário | register route |
| E-mail | **Obrigatório** | Formato de e-mail válido, ≤255 caracteres; um e-mail só pode registrar uma conta | register route |
| Código de verificação de e-mail | **Obrigatório** | 6 dígitos; **válido por 10 minutos**; invalidado após a verificação; reenviar marca o código antigo como usado | `src/lib/email-verification.ts` |
| Telefone | Opcional | Número da China continental começando com `1[3-9]`, 11 dígitos no total; um telefone só pode ser vinculado a uma conta | register route |

A página também oferece três botões de login de terceiros: **Google, Watcha, conta Huawei** (`GoogleSignInButton` / `WatchaLoginButton` / `HuaweiLoginButton`). Contas de terceiros não têm senha local; tentar fazer login com senha depois retorna « 该账号未设置密码，请使用其他方式登录 » (Esta conta não tem senha definida, use outro método de login).

## Limites de frequência e parâmetros anti-força bruta

| Comportamento | Limite | Fonte |
|---|---|---|
| Envio do registro | **3 vezes/min/IP**, 429 ao exceder | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Enviar código de verificação | Mesmo IP 1 vez/min **e** mesmo e-mail 1 vez/min, 429 ao exceder; contagem regressiva de 60 segundos no botão do frontend | `src/app/api/auth/register/send-code/route.ts` |
| Verificação do código | Máximo **5 tentativas** por e-mail em 10 minutos; ao atingir o limite, recusado mesmo com o código correto — é preciso um novo código | `src/lib/email-verification.ts` |
| Código de esqueci a senha | 1 vez/min/IP | `src/app/api/auth/forgot-password/route.ts` |
| Login | 5 vezes/min/IP; **5 falhas seguidas bloqueiam a conta por 30 minutos** (423), com aviso decrescente de tentativas restantes | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Comportamento de proteção de privacidade**: ao enviar o código de verificação / esqueci a senha, a interface retorna a mesma mensagem de sucesso estando o e-mail registrado ou não, sem revelar se a conta existe.

## Transição de status após um registro bem-sucedido

1. O usuário é salvo com `accountStatus: 'pending'` e **3 distintivos iniciais** (register route).
2. O servidor também define dois cookies HttpOnly: JWT (permite acessar `/subscription` diretamente) e pendingUserToken (credencial de identidade para o fluxo de assinatura).
3. A página de registro detecta `pending_payment` → pula para `/subscription` (preservando o parâmetro de retorno `next`).
4. Pagamento concluído → `accountStatus` passa a `active` (PayPal ativa automaticamente via Webhook; QR code WeChat por confirmação manual; IAP Huawei via `activate-huawei`). Ver `payment-and-activation.md`.

As chamadas de um usuário não ativado (pending) às APIs principais (feed, mapa, chat com humanos digitais, check-ins, etc.) retornam sempre 403; os links de posts compartilhados são a exceção (continuam acessíveis publicamente).

## Tabela de erros comuns

| Mensagem | Causa | O que fazer |
|---|---|---|
| 「用户名已存在」(O nome de usuário já existe) | Nome de usuário ocupado (sem diferenciar maiúsculas) | Escolha outro nome de usuário |
| 「邮箱已被使用」(O e-mail já está em uso) | E-mail já registrado | Use outro e-mail; ou entre pelo login + « Esqueci a senha » para recuperar a conta antiga |
| 「邮箱验证码错误或已过期」(O código de verificação de e-mail está incorreto ou expirou) | Código digitado errado / mais de 10 minutos / recusado após mais de 5 tentativas | Clique em « Reenviar » e use o código do **último** e-mail |
| Não recebo o código de verificação | Limite de 60 segundos; ou caiu no spam/promoções | Espere a contagem regressiva terminar para reenviar; confira a pasta de spam |
| 「手机号已被使用」(O telefone já está em uso) | Telefone vinculado a outra conta | Remova o telefone (campo opcional) ou use outro número |
| 「注册请求过于频繁」/ 429 (Solicitações de registro muito frequentes) | Atingiu o limite de 3 registros/min/IP | Espere alguns minutos e tente novamente |
| 409「用户名或邮箱已被注册」(Nome de usuário ou e-mail já registrados) | Colisão com outro usuário no envio (fallback de concorrência) | Mude o nome de usuário ou o e-mail e tente novamente |
| 「图片大小不能超过5MB」/「不支持 SVG」(O tamanho da imagem não pode exceder 5MB / SVG não suportado) | Avatar fora das regras | Troque a imagem ou pule o avatar |
| Registro bem-sucedido mas login 403「请完成订阅以激活账户」(Conclua sua assinatura para ativar a conta) | A conta ainda está pending | Após o login, siga o aviso na página e vá em `/subscription` para concluir a assinatura |
| Login 423「账户已锁定」(Conta bloqueada) | Senha errada 5 vezes | Espere 30 minutos |
| Login 401「还剩 N 次尝试机会」(Restam N tentativas) | Senha errada, perto do bloqueio | Pense bem antes de tentar de novo, ou vá direto ao « Esqueci a senha » |
| 「该账号未设置密码，请使用其他方式登录」(Esta conta não tem senha definida, use outro método de login) | Conta de terceiros (Google/Watcha/Huawei) | Faça login com o botão de terceiros original |
| 「该账号已注销」(Esta conta foi desativada) | Conta desativada | É preciso se registrar novamente |

## Dicas de login (úteis também para resolver problemas)

O login aceita um campo combinado de **nome de usuário / e-mail / telefone** (qualquer um dos três funciona como nome da conta).
Esqueci a senha: página de login → « Esqueci a senha » → informe o e-mail de registro, receba um código de 6 dígitos → redefina.