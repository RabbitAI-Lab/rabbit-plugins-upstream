# Diagnóstico de Funil, Fricção Pós-Clique & Otimização de Conversão para SaaS / APIs

Este guia estabelece os protocolos de diagnóstico e as soluções arquiteturais para quando campanhas de Meta Ads apresentam excelentes métricas de topo de funil (CTR alto > 3-5%, CPC baixo R$ 0,10 - R$ 0,15), mas baixa taxa de conversão final (Sign Up / Vendas) no destino.

---

## 1. O Diagnóstico dos 4 Gargalos Críticos de Pós-Clique

Quando o tráfego é barato e qualificado, a perda de conversão ocorre invariavelmente na experiência de destino:

### A. Redirecionamento com Aba Incorreta ("Entrar" vs "Criar Conta")
- **Sintoma:** O visitante clica em um anúncio ("Testar Z-AI"), clica no CTA da landing page e é direcionado para a rota `/auth`, onde a aba padrão ativa é "Entrar / Sign In".
- **Impacto:** Mais de 60% do tráfego frio mobile desiste na hora por achar que precisa de login existente ou convite prévio.
- **Regra:** Todos os links de landing pages, anúncios e botões de ação externa devem forçar a aba de cadastro (`/auth?tab=signup` ou `/auth?plan=...`).

### B. Fricção Prematura de Dados Fiscais (CPF / CNPJ)
- **Sintoma:** Exigir documento fiscal (CPF/CNPJ) no primeiro formulário de criação de conta.
- **Impacto:** Em tráfego pago para SaaS/API, a exigência de CPF antes de conhecer o produto gera desconfiança imediata e abandono.
- **Regra:** 
  1. O cadastro inicial (Sign Up) deve exigir apenas **Nome, WhatsApp/DDI, E-mail e Senha**.
  2. O CPF/CNPJ deve ser solicitado exclusivamente no momento do checkout/pagamento na tela de Billing/Faturamento ou ser estritamente opcional no registro inicial.
  3. Para clientes internacionais (DDI ≠ +55), campos de identificação fiscal (SSN/Tax ID) devem ser sempre opcionais.

### C. Fricção de Navegação Multi-Página (Page Hop)
- **Sintoma:** Anúncio ➔ Landing Page ➔ Clique no CTA ➔ Carregamento de `/auth` ➔ Preenchimento ➔ Submit.
- **Solução de Alta Conversão:** **Formulário Inline On-Page (`#cadastro`)**.
  - O formulário fica embutido na própria landing page do produto.
  - Todos os CTAs da página executam rolagem suave (`scrollIntoView({ behavior: 'smooth' })`) direto para a âncora `#cadastro`.
  - Fallback automático: se o elemento `#cadastro` não estiver na DOM, redireciona para `/auth?tab=signup&plan=...`.

### D. Falta de Auto-Login Instantâneo
- **Sintoma:** Após preencher o cadastro, o usuário é jogado para uma tela pedindo para confirmar e-mail ou fazer login novamente.
- **Solução:** Autenticação imediata via Supabase Auth + redirecionamento instantâneo para `/dashboard`, pronto para testar o produto/playground.

---

## 2. Arquitetura de Implementação: Formulário Inline + Auto-Login (React + Supabase)

### A. Estrutura do Componente Inline On-Page
```tsx
// Exemplo em src/routes/z-ai.tsx
const [plan, setPlan] = useState<'voice_starter' | 'whatsapp_basic'>('voice_starter');
const [ddi, setDdi] = useState('55');
const [phone, setPhone] = useState('');
const [name, setName] = useState('');
const [email, setEmail] = useState('');
const [password, setPassword] = useState('');
const [loading, setLoading] = useState(false);

const handleSignup = async (e: React.FormEvent) => {
  e.preventDefault();
  setLoading(true);
  try {
    const cleanPhone = phone.replace(/\D/g, '');
    const fullPhone = cleanPhone ? `${ddi}${cleanPhone}` : '';

    // 1. Supabase SignUp com metadados de atribuição e plano
    const { data, error } = await supabase.auth.signUp({
      email: email.trim().toLowerCase(),
      password: password.trim(),
      options: {
        emailRedirectTo: `${window.location.origin}/dashboard`,
        data: {
          full_name: name.trim(),
          phone: fullPhone,
          plan_id: plan,
          source: 'inline_landing',
        },
      },
    });

    if (error) throw error;

    // 2. Disparo de Evento Meta Pixel
    if (typeof window !== 'undefined' && (window as any).fbq) {
      (window as any).fbq('track', 'CompleteRegistration', {
        content_name: plan === 'voice_starter' ? 'Z-AI Voice + WhatsApp' : 'WhatsApp API',
        currency: 'BRL',
        value: plan === 'voice_starter' ? 49.90 : 14.90,
      });
    }

    // 3. Auto-Login Imediato e Redirecionamento
    if (data.session) {
      navigate({ to: '/dashboard' });
    } else {
      const { error: signInError } = await supabase.auth.signInWithPassword({
        email: email.trim().toLowerCase(),
        password: password.trim(),
      });
      if (!signInError) {
        navigate({ to: '/dashboard' });
      } else {
        navigate({ to: '/auth?tab=signin' });
      }
    }
  } catch (err: any) {
    toast.error(err.message || 'Erro ao criar conta.');
  } finally {
    setLoading(false);
  }
};
```

### B. Função de Smooth Scroll em Todos os CTAs
```tsx
const scrollToSignup = (e: React.MouseEvent) => {
  const el = document.getElementById('cadastro');
  if (el) {
    e.preventDefault();
    el.scrollIntoView({ behavior: 'smooth' });
  }
};
```

---

## 3. Template de Relatório Executivo WhatsApp (PAPI MCP)

Ao emitir alertas de auditoria de tráfego pago para stakeholders via WhatsApp, utilize a estrutura:

```text
🚀 *RELATÓRIO DE DESEMPENHO — META ADS PAPI*

📊 *Métricas Consolidadas:*
• *Investimento Total:* R$ 43,93
• *Impressões:* 24.500
• *Cliques no Link:* 353
• *CPC Médio:* R$ 0,12
• *CTR Geral:* 2,12% (Pico de *5,21%* no Anúncio de Voz com IA)

🎯 *Destaques de Performance:*
1. *AD 02 (Voz com IA - R$ 49,90):* Maior engajamento (CTR 5,21% no público de Devs).
2. *AD 01 (WhatsApp API - R$ 14,90):* Excelente volume de cliques com CPC de R$ 0,11.

🛠️ *Ações Executadas & Otimizações:*
• *Saldo Recarregado:* R$ 50,01 adicionados via PIX, veiculação 100% normalizada.
• *Orçamento:* Ajustado para R$ 10,00/dia por conjunto (R$ 20,00/dia total).
• *Otimização de Conversão:* Implementado formulário rápido inline na landing page `/z-ai` com login automático pós-cadastro.
```
