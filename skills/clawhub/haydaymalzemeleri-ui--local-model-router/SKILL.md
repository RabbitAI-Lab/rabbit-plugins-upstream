---
name: "local-model-router"
description: "API maliyetini düşürmek için basit sorguları yerel Ollama modellerine yönlendirir"
---

# Local Model Router Skill

## Amaç
DeepSeek cloud API maliyetini azaltmak için basit/orta düzey sorguları yerel Ollama modellerine yönlendirir. Zensa ana orkestratör olarak kalır, sadece response üretimi için local modelleri kullanır.

## Model Görev Dağılımı

| Görev Türü | Model | Açıklama |
|:-----------|:------|:---------|
| Selamlaşma / basit muhabbet | `phi4-mini:latest` | Hızlı, doğal Türkçe, düşük CPU |
| Bilgi sorusu / açıklama | `phi4-mini:latest` veya `qwen2.5-coder:7b` | Orta karmaşıklık |
| Kod yazma / düzeltme | `qwen2.5-coder:7b` | Code-specialized model |
| Mantık / problem çözme | `deepseek-r1:14b` | Reasoning özellikli |
| Embedding / vektör arama | `nomic-embed-text:latest` | 274MB, çok hızlı |
| **Karmaşık / araçlı / çok adımlı** | **DeepSeek cloud** | Tool calling, dosya işlemleri, cron vs. |

## Kullanım

### 1. Local model çağırma (API üzerinden)
```bash
curl -s http://localhost:11434/api/generate \
  -d '{"model":"phi4-mini:latest","prompt":"...","stream":false,"options":{"num_ctx":131072}}'
```

### 2. Router karar mantığı

Zensa mesajı alır, analiz eder:
1. **Tool/araç gerekiyor mu?** → DeepSeek cloud
2. **Karmaşık planlama / çok adımlı iş?** → DeepSeek cloud
3. **Selam / kısa muhabbet?** → phi4-mini (yerel)
4. **Kod sorusu / düzeltmesi?** → qwen2.5-coder (yerel)
5. **Mantık / matematik sorusu?** → deepseek-r1 (yerel)
6. **Normal bilgi sorusu** → phi4-mini (yerel)

### 3. Fallback
Yerel model yetersiz kalırsa (hata, anlamsız cevap) → DeepSeek cloud'a düş.

## Maliyet Karşılaştırması

| Senaryo | DeepSeek (cloud) | Yerel model |
|:--------|:----------------:|:-----------:|
| "Selam, nasılsın?" | $0.0005 | **$0** |
| "Python'da fibonacci yaz" | $0.002 | **$0** |
| Basit bilgi sorusu | $0.001 | **$0** |
| Karmaşık analiz | $0.01 | $0 (deepseek-r1) |
| **Günlük ~100 mesaj** | **~$0.50** | **$0.05** (sadece elektrik) |

## Sınırlamalar
- Yerel modeller tool calling desteklemez → araç gerektiren işlerde DeepSeek cloud kullanılır
- Büyük context gerekiyorsa (64K+) → DeepSeek cloud (1M context)
- Çok dilli / güncel bilgi gerekiyorsa → DeepSeek cloud
