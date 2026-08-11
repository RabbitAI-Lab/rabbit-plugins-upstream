#!/usr/bin/env node
/**
 * explore-platform.js — Agent-guided platform exploration helper.
 *
 * This script doesn't run autonomously. It outputs guidance for an AI agent
 * to explore a new procurement platform and create an adapter.
 *
 * Usage with an AI agent:
 *   node explore-platform.js --url https://new-platform.ggzy.gov.cn/
 *
 * The agent will:
 *   1. Navigate to the platform
 *   2. Find the procurement listing page
 *   3. Identify extraction selectors
 *   4. Test pagination
 *   5. Generate adapter code
 */

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

/**
 * Generate exploration guidance for an AI agent.
 */
function generateGuidance(url, platformName) {
  return `
## Platform Exploration Task

**Target URL**: ${url}
**Platform Name**: ${platformName || 'TBD'}

### Step 1: Navigate & Survey
1. Go to ${url}
2. Identify the procurement/tender announcement listing page
3. Note the URL pattern for listing pages (is it /index.html, /list?page=1, etc?)
4. Check if there's a search/filter mechanism

### Step 2: Extract Selectors
Use browser DevTools to identify:
- **Item container**: CSS selector for each result row (e.g., 'li.search-row', '.publicont', 'tr')
- **Title link**: Selector for the title anchor (e.g., 'a.mya', 'h4 a')
- **Date element**: Selector for the publication date (e.g., '.content-date', '.span_o')
- **URL attribute**: How to get the detail URL (href, data-infourl, etc.)

### Step 3: Test Pagination
- How does pagination work? (URL-based like /page_2.html? Click-based?)
- Selector for "next page" button (e.g., 'a:has-text("下一页")', '.ant-pagination-next')
- Max pages before results go out of date window?

### Step 4: Create Adapter
\`\`\`bash
bidding-hunter create-adapter --name ${platformName || 'new-platform'}
\`\`\`

Then implement these in the generated file:
1. Replace extractItems() with actual selectors
2. Implement scan() pagination logic  
3. Set meta.url to actual listing URL

### Step 5: Test
\`\`\`bash
bidding-hunter test-platform --name ${platformName || 'new-platform'}
\`\`\`
`;
}

/**
 * Quick reconnaissance: open the URL and capture page structure hints.
 * Useful for pre-filling adapter with discovered selectors.
 */
async function quickRecon(url) {
  let browser;
  try {
    try {
      browser = await chromium.launch({
        headless: true,
        executablePath: '/snap/bin/chromium',
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
      });
    } catch {
      browser = await chromium.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
      });
    }

    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await page.waitForTimeout(3000);

    const hints = await page.evaluate(() => {
      // Find common link patterns
      const links = Array.from(document.querySelectorAll('a[href]'));
      const bidLinks = links.filter(l => {
        const text = l.textContent.trim();
        return text.length > 10 && /招标|采购|公告|磋商|谈判/.test(text);
      });

      // Detect pagination
      const pagination = {
        hasNextPage: Boolean(document.querySelector('.ant-pagination-next, a:has-text("下一页"), li.next a')),
        hasPageNumbers: Boolean(document.querySelector('.ant-pagination, .paging, .pagination')),
      };

      // Detect table structure
      const tables = document.querySelectorAll('table, .ant-table, [class*="table"]');
      const hasTable = tables.length > 0;

      // Common container patterns
      const containers = [];
      for (const sel of ['li.search-row', '.publicont', '.result-item', '.list-item', 'tr[onclick]']) {
        const count = document.querySelectorAll(sel).length;
        if (count > 0) containers.push({ selector: sel, count });
      }

      return {
        totalLinks: links.length,
        procurementLinks: bidLinks.length,
        sampleLinks: bidLinks.slice(0, 3).map(l => ({
          text: l.textContent.trim().substring(0, 80),
          href: l.href.substring(0, 80),
        })),
        pagination,
        hasTable,
        containers,
        title: document.title,
      };
    });

    await browser.close();
    return hints;
  } catch (error) {
    if (browser) await browser.close();
    return { error: error.message };
  }
}

// --- CLI ---
if (require.main === module) {
  const args = process.argv.slice(2);
  let url = null;
  let name = null;
  let recon = false;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--url' || args[i] === '-u') url = args[++i];
    else if (args[i] === '--name' || args[i] === '-n') name = args[++i];
    else if (args[i] === '--recon' || args[i] === '-r') recon = true;
    else if (!url && args[i].startsWith('http')) url = args[i];
  }

  if (!url) {
    console.error('Usage: node explore-platform.js --url <url> [--name <name>] [--recon]');
    process.exit(1);
  }

  console.log(generateGuidance(url, name));

  if (recon) {
    console.log('Running quick reconnaissance...\n');
    quickRecon(url).then(hints => {
      console.log(JSON.stringify(hints, null, 2));
    }).catch(err => {
      console.error(`Recon failed: ${err.message}`);
    });
  }
}

module.exports = { generateGuidance, quickRecon };
