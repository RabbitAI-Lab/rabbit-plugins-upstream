# AI Agent Navigation & Chemical Extraction Masterclass (v2.36.1)

This guide provides operational intelligence for AI Agents crawling, navigating, and extracting chemical offerings from Iranian supplier platforms. It teaches the agent how to identify website structures, manipulate pagination controls (Next/Prev, Load More, Infinite Scroll), bypass regional geo-fencing barriers via sanctioned relays, and extract chemical data (CAS, purity, packaging, pricing) with zero hallucination.

---

## 1. Network Topology & Geo-Fencing Realities

### 1.1 The Iranian National Information Network (SHOMA / NIN)
Many Iranian e-commerce platforms and chemical distributors are hosted inside the National Information Network (NIN). Edge firewalls routinely drop TCP SYN packets or terminate TLS handshakes from international datacenter IP addresses (AWS, GCP, DigitalOcean, Hetzner, Oracle Cloud).

### 1.2 The Relay Infrastructure
To fetch geo-fenced public catalogues without unauthorized access or policy violations, the system utilizes a multi-layered relay mesh of public services whose egress IPs are whitelisted by Iranian edge ACLs:
1. **Google Translate Domain-Mirror Relay (`translate_goog`)**:
   `https://{dashed-host}.translate.goog/{path}?_x_tr_sl=fa&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp`
   Google's translation crawlers fetch the page server-side. Renders full HTML including footer contacts, Persian text, and IRR pricing.
2. **Jina AI Reader (`jina`)**:
   `https://r.jina.ai/{url}`
   Returns markdown representations of web pages, stripping clutter and isolating catalogue content.
3. **Internet Archive Wayback Machine (`wayback` & `spn2`)**:
   `https://web.archive.org/web/{ts}id_/{url}`
   Reads immutable historical snapshots or triggers fresh captures via Save Page Now (SPN2).
4. **Common Crawl Index & WARC Store (`commoncrawl`)**:
   Fetches raw WARC records via byte-range requests from AWS S3.
5. **Google AMP CDN Cache (`amp_cache`)**:
   `https://{dashed-host}.cdn.ampproject.org/c/s/{host}{path}`
   Serves pre-rendered mobile/AMP snapshots from Google edge servers (<300ms).
6. **Arquivo.pt Portuguese National Archive (`arquivo_pt`)**:
   Independent European crawler infrastructure with snapshots of `.ir` domains.

---

## 2. Platform Architecture & Navigation Strategies

### 2.1 WooCommerce / WordPress Storefronts (`family: woocommerce`)
The majority of commercial chemical retailers in Iran operate WooCommerce.

#### Priority 1: Direct Store REST API (Zero HTML Parsing)
Always attempt the public WooCommerce Store API first:
```http
GET /wp-json/wc/store/v1/products?per_page=100&page=N
```
- **Stopping condition**: Check response header `X-WP-TotalPages`. When `page == X-WP-TotalPages`, stop. If the header is absent, stop when the returned JSON array is empty `[]` or has length `< 100`.
- **Product Total**: The header `X-WP-Total` contains the exact total molecule/product count.
- **Product Details**:
  - `name`: Product title (often contains brand and grade, e.g., "استون گرید HPLC مرک").
  - `sku`: Supplier internal catalogue number (note: this is a vendor SKU, **not** a CAS number).
  - `prices.price`: Price in minor currency units (divide by 100).
  - `prices.currency_code`: Usually `IRR` or `IRT` (Toman).
  - `is_in_stock`: Boolean inventory flag.
  - `description` / `short_description`: Full text containing CAS, chemical formula, and purity.

#### Priority 2: Product Sitemaps
If `/wp-json` returns 401/403/404:
- Fetch `/product-sitemap.xml` or `/sitemap_index.xml`.
- Extract all `<loc>` elements matching `/product/`, `/محصول/`, or `/products/`.
- Filter out non-product URLs (`/category/`, `/tag/`, `/page/`).

#### Priority 3: HTML Pagination Fallback
When parsing WooCommerce HTML category pages:
- **URL Path Pattern**: `/shop/page/N/` or `/product-category/{slug}/page/N/`.
- **Query Parameter Pattern**: `?paged=N` or `?product-page=N`.
- **Next Page Selector**: `a.next.page-numbers`, `a[rel="next"]`, `.woocommerce-pagination a.next`.

---

### 2.2 Static & Tabular Listings (`family: static_listing`)
Industrial suppliers often display products in HTML tables.

#### Table Structure
A typical Iranian chemical table has the following column headers:
| Persian Header | Transliteration | English Meaning | Extraction Target |
|---|---|---|---|
| نام محصول / عنوان | Nam-e Mahsool | Product Name | Chemical compound name |
| کد محصول / آرتیکل | Code / Article | Article / Catalog Number | Vendor Catalog SKU (e.g. Merck 100014) |
| شماره CAS | Shomare CAS | CAS Registry Number | Chemical identity anchor |
| گرید / درجه خلوص | Grade / Darsad Kholoos | Grade / Purity | ACS, GR, HPLC, Tech, % |
| بسته‌بندی | Basteh-bandi | Packaging | 1kg, 2.5L, 25kg drum |
| وضعیت | Vaziat | Inventory Status | موجود (In stock) / ناموجود |
| قیمت | Gheymat | Price | IRR / Toman or استعلام |

#### Numbered Pagination Mechanics
1. **Locate Pager Block**: Look for `.pagination`, `.pager`, `.nav-links`, or `ul.page-numbers`.
2. **Find Active Page**: Identify `.current`, `.active`, or `span.page-numbers.current`. Let current page be $P$.
3. **Identify Next Target**:
   - Check for explicit Next link: `a.next` or link containing `بعدی`.
   - If absent, locate adjacent numeric link $P+1$.
   - **Crucial Guard**: Never jump to the maximum number visible in the pager if it is far from $P$ (e.g., if on page 2 and links show `1, 2, 3 ... 54`, the "54" is the tail, not the next page). Advance strictly step-by-step ($P+1$).
4. **Detect Last Page**:
   - Next button has class `disabled` or attribute `aria-disabled="true"`.
   - The page content hash is identical to the previous page (pager dead-end trap).
   - The product table body is empty.

---

### 2.3 AJAX "Load More" & Infinite Scroll (`family: load_more / infinite_scroll`)

#### Reversing "Load More" Buttons
Do not invoke heavy browser engines if an API replay is possible.
1. Inspect the button element:
   ```html
   <button class="btn-load-more" data-page="1" data-max="12" data-cat="45" data-url="/ajax/load-products">
       نمایش بیشتر
   </button>
   ```
2. Replay the request directly:
   ```http
   GET /ajax/load-products?page=2&cat=45 HTTP/1.1
   X-Requested-With: XMLHttpRequest
   ```
   Or WordPress admin AJAX:
   ```http
   POST /wp-admin/admin-ajax.php HTTP/1.1
   Content-Type: application/x-www-form-urlencoded

   action=load_more_products&paged=2&category=45
   ```

#### Headless Browser Infinite Scroll (Playwright Execution)
When API reverse-engineering is infeasible:
1. Initialize headless Chromium with viewport 1280x800.
2. Scroll to bottom in increments:
   ```python
   previous_height = await page.evaluate("document.body.scrollHeight")
   while scroll_iterations < max_scroll:
       await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
       await page.wait_for_timeout(1000)
       new_height = await page.evaluate("document.body.scrollHeight")
       if new_height == previous_height:
           # Check for "Load More" button that may have appeared
           load_btn = await page.query_selector("button:has-text('نمایش بیشتر'), .load-more")
           if load_btn and await load_btn.is_visible():
               await load_btn.click()
               await page.wait_for_timeout(1500)
               new_height = await page.evaluate("document.body.scrollHeight")
           else:
               break  # Truly reached end of catalogue
       previous_height = new_height
   ```
3. Extract all product card DOM nodes.

---

### 2.4 Legacy ASP.NET WebForms (`family: aspnet`)
Commonly found on older municipal and petrochemical supply sites.
- **Form Action**: Pagination does not change the URL; it triggers `__doPostBack`.
- **Viewstate Replay**:
  Extract `__VIEWSTATE`, `__EVENTVALIDATION`, and `__VIEWSTATEGENERATOR` from hidden `<input>` elements.
  Submit a POST request to the current URL with:
  ```
  __EVENTTARGET = ctl00$MainContent$GridView1
  __EVENTARGUMENT = Page$2
  __VIEWSTATE = <extracted_viewstate>
  __EVENTVALIDATION = <extracted_validation>
  ```
- **Error Trap**: ASP.NET sites frequently return HTTP 200 for error/empty pages with text `Server Error in '/' Application` or `<title>404</title>`. Check response body text before parsing.

---

## 3. Universal Persian Navigation Lexicon

AI Agents must match both Latin and Persian strings when locating UI controls:

| Category | Persian Script | Transliteration | English Equivalents | Standard CSS Selectors |
|---|---|---|---|---|
| **Next** | بعدی | Ba'di | Next | `a.next`, `a[rel="next"]`, `.next-page` |
| | صفحه بعد | Safheye Ba'd | Next Page | `.pagination-next` |
| | صفحه بعدی | Safheye Ba'di | Next Page | `a:has-text('بعدی')` |
| **Previous** | قبلی | Ghabli | Prev, Previous | `a.prev`, `a[rel="prev"]` |
| | صفحه قبل | Safheye Ghabl | Previous Page | `.pagination-prev` |
| **Load More**| نمایش بیشتر | Namayesh-e Bishtar | Show More | `button.load-more`, `.btn-more` |
| | مشاهده بیشتر | Moshahadeh-ye Bishtar| View More | `a.view-more` |
| | بارگذاری بیشتر| Bargozari-ye Bishtar | Load More | `button:has-text('بیشتر')` |
| | موارد بیشتر | Mavared-e Bishtar | More Items | `.ajax-load-more` |
| **First/Last**| اولین صفحه | Avvalin Safheh | First Page | `a.first`, `.page-first` |
| | آخرین صفحه | Akharin Safheh | Last Page | `a.last`, `.page-last` |
| **Stock** | موجود | Mojood | In Stock | `.in-stock`, `span.badge-success` |
| | ناموجود | Na-mojood | Out of Stock | `.out-of-stock`, `.badge-danger` |
| | عدم موجودی | Adam-e Mojoodi | Unavailable | `span:has-text('ناموجود')` |
| **Price** | استعلام قیمت | Estelam-e Gheymat | Call for Price | `.call-for-price`, `a.inquiry` |
| | تماس بگیرید | Tamas Begirid | Contact Us | `.price-contact` |
| | توافقی | Tavafoghi | Negotiable | `span:has-text('تماس')` |

---

## 4. Chemical Informatics & Extraction Logic

### 4.1 CAS Registry Number Validation
Never trust arbitrary hyphenated numbers. A genuine CAS Registry Number has the format:
$$\text{Digits}_{2\text{ to }7} - \text{Digits}_2 - \text{Digit}_1$$

#### Algorithmic Luhn Checksum Verification:
For a candidate CAS $d_k d_{k-1} \dots d_2 d_1 - d_0$:
$$\left( \sum_{i=1}^k i \times d_i \right) \pmod{10} = d_0$$

#### Python Implementation for Agents:
```python
import re

CAS_REGEX = re.compile(r"\b([1-9]\d{1,6})-(\d{2})-(\d)\b")

def validate_cas(cas_str: str) -> bool:
    """Validate CAS Registry Number format and checksum."""
    m = CAS_REGEX.fullmatch(cas_str.strip())
    if not m:
        return False
    part1, part2, check_digit = m.groups()
    digits = [int(c) for c in (part1 + part2)]
    check = int(check_digit)
    # Reverse digits so d1 is at index 0, d2 at index 1, etc.
    digits.reverse()
    total = sum((i + 1) * digit for i, digit in enumerate(digits))
    return (total % 10) == check
```
*Example*: Acetone is `67-64-1`. Digits before check: `[6, 7, 6, 4]`.
Reversed: `4, 6, 7, 6`.
$\text{Sum} = (1 \times 4) + (2 \times 6) + (3 \times 7) + (4 \times 6) = 4 + 12 + 21 + 24 = 61$.
$61 \pmod{10} = 1 \implies \mathbf{Valid}$.

---

### 4.2 Grade & Purity Disambiguation
Extract and classify the purity grade from the product title, specs, or table column:

1. **Analytical & Research Grades**:
   - `ACS`: Meets American Chemical Society specifications.
   - `GR` / `Garantieschein`: Merck analytical reagent grade.
   - `AR` / `Analytical Reagent`: Standard analytical laboratory grade.
   - `HPLC` / `Chromatography`: High-performance liquid chromatography solvent.
   - `Spectroscopy` / `UV`: UV/Vis spectrometry grade.
   - Persian keywords: `خلوص بالا`, `گرید تحلیلی`, `آزمایشگاهی`.
2. **Pharmacopeial Grades**:
   - `USP` (United States Pharmacopeia)
   - `BP` (British Pharmacopoeia)
   - `EP` / `Ph. Eur.` (European Pharmacopoeia)
   - Persian keywords: `گرید دارویی`, `فارماکوپه`.
3. **Industrial & Technical Grades**:
   - `Technical` / `Tech`: Technical/industrial raw input.
   - `Industrial`: Bulk processing chemical.
   - Persian keywords: `صنعتی`, `تجاری`, `تکنیکال`.

---

### 4.3 Packaging Size & Quantity Normalization
Extract the quantity and convert to standard metric units:

| Pattern | Target Unit | Multiplier to Base Unit (g or mL) | Persian Equivalents |
|---|---|---|---|
| `(\d+(?:\.\d+)?)\s*kg` | kg | $1000\text{ g}$ | کیلوگرم, کیلو |
| `(\d+(?:\.\d+)?)\s*g\b` | g | $1\text{ g}$ | گرم |
| `(\d+(?:\.\d+)?)\s*mg` | mg | $0.001\text{ g}$ | میلی‌گرم |
| `(\d+(?:\.\d+)?)\s*ton` | ton | $1,000,000\text{ g}$ | تن |
| `(\d+(?:\.\d+)?)\s*L\b` | L | $1000\text{ mL}$ | لیتر |
| `(\d+(?:\.\d+)?)\s*mL` | mL | $1\text{ mL}$ | میلی‌لیتر, سی‌سی |
| `بشکه\s*(\d+)` | drum | Industrial drum packaging | بشکه |
| `کیسه\s*(\d+)` | bag | Industrial bag packaging | کیسه |
| `گالن\s*(\d+)` | gallon | Liquid gallon container | گالن |

---

### 4.4 Currency & Price Calculations
- **Currency Identification**:
  - `ریال` (IRR): The official national currency.
  - `تومان` (IRT / Toman): The common merchant denomination.
  - **Conversion Formula**:
    $$\text{Price in IRR} = \text{Price in Toman} \times 10$$
  - *Example*: `۵۵۰,۰۰۰ تومان` $\to 550,000\text{ Toman} = 5,500,000\text{ IRR}$.
- **Call for Price**:
  If the price text contains `استعلام قیمت`, `تماس بگیرید`, or `توافقی`, set `price = None` and record `offer_type = "inquiry"`.

---

### 4.5 Persian-to-IUPAC Common Chemical Map
Iranian suppliers frequently list chemicals using colloquial Persian chemical trade names:

| Persian Name | Transliteration | IUPAC / English Equivalent | Canonical CAS |
|---|---|---|---|
| سود پرک / سود سوزآور | Sood-e Parak | Sodium Hydroxide | `1310-73-2` |
| اسید کلریدریک / جوهر نمک | Asid Chloridric / Johar Namak | Hydrochloric Acid | `7647-01-0` |
| اسید سولفوریک / جوهر گوگرد | Asid Sulfuric / Johar Googerd | Sulfuric Acid | `7664-93-9` |
| اسید نیتریک / جوهر شوره | Asid Nitric / Johar Shooreh | Nitric Acid | `7697-37-2` |
| استون | Aseton | Acetone | `67-64-1` |
| متانول / الکل صنعتی | Metanol / Alkol-e San'ati | Methanol | `67-56-1` |
| اتانول / الکل سفید | Etanol / Alkol-e Sefid | Ethanol | `64-17-5` |
| زانتان گام / صمغ زانتان | Xanthan Gum / Samgh-e Xanthan| Xanthan Gum | `11138-66-2` |
| تگزاپون / سدیم لوریل اتر سولفات | Texapon / SLES | Sodium Lauryl Ether Sulfate| `68585-34-2` |
| آب اکسیژنه / هیدروژن پراکسید | Ab-e Oksizheneh | Hydrogen Peroxide | `7722-84-1` |
| آب ژاول / وایتکس | Ab-e Zhavel / Vitex | Sodium Hypochlorite | `7681-52-9` |
| تیتان / دی اکسید تیتانیوم | Titan / Di-oksid Titan | Titanium Dioxide | `13463-67-7` |
| اسید فسفریک | Asid Phosphoric | Phosphoric Acid | `7664-38-2` |
| کربنات سدیم / سودا اش | Carbonat-e Sodiom / Soda Ash | Sodium Carbonate | `497-19-8` |
| پرکلرواتیلن | Perchloroetilen | Tetrachloroethylene | `127-18-4` |
| کلرید پتاسیم | Chlorid-e Potasiom | Potassium Chloride | `7447-40-7` |

---

## 5. Saturation Mitigation & Dynamic Failover

### 5.1 Real-Time Circuit Breaker
When executing crawls, never repeat requests to an origin or relay that is returning HTTP 429 (Too Many Requests), HTTP 503 (Service Unavailable), or CAPTCHA pages.

1. **Immediate Demotion**:
   The `AdaptiveSelector` tracks error strikes. On receiving a 429:
   - If a `Retry-After` header is present, enforce a cooldown of `now + Retry-After`.
   - If absent, trigger escalating cooldown ($60\text{s} \to 120\text{s} \to 300\text{s}$).
2. **Instant Alternative Switching**:
   Do not pause the crawl. The engine immediately queries the site's personalized chain:
   $$\text{Primary (Saturated)} \xrightarrow{\text{Demote}} \text{Next Best Profiled Alternative}$$
   *Example*: If `translate_goog` hits 429 on `tamadkala.com`, the worker immediately routes the next request to `jina` or `wayback`.
3. **Concurrency Slot Throttling**:
   Every relay method has an active lease cap (e.g., max 6 concurrent connections for `translate_goog`, max 3 for `jina`). If the slot is full, the selector reports `SATURATED (concurrency full)`, and the worker picks an alternate method without waiting.
4. **Zero-Timer Token Bucket**:
   Static `time.sleep(0.5)` calls are replaced with `GLOBAL_LIMITER.acquire()`. If requests are naturally spaced or burst capacity is available, execution proceeds with **0 ms delay**, maximizing download throughput.

---

## 6. Summary: The 5-Step Golden Flow for Agents

1. **Probe Profile**: Query `AdaptiveSelector.select(host)` to get the personalized method chain.
2. **Cheapest Path First**: Check WooCommerce REST API `/wp-json/wc/store/v1/products` or XML sitemaps before scraping HTML.
3. **Follow Natural Pagers**: Advance pagination using `page=N+1` or `.next`, checking `X-WP-TotalPages` or content-hash stops.
4. **Validate Chemical Identifiers**: Verify CAS checksums and isolate analytical grades from raw titles.
5. **Fail-Closed Gate**: Enforce Iran-only supplier admission (Enamad, +98 phone, IRR currency, Persian catalogue text) before committing data to the database.
