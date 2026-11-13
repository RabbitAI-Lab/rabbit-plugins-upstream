/**
 * Broken Link Checker Skill
 * Checks for broken links in documentation and markdown files
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

/**
 * Extract all links from a markdown file
 * @param {string} content - File content
 * @returns {Array} Array of link objects
 */
function extractLinks(content) {
  const links = [];
  
  // Match markdown links: [text](url)
  const markdownLinkRegex = /\[([^\]]+)\]\(([^)]+)\)/g;
  let match;
  while ((match = markdownLinkRegex.exec(content)) !== null) {
    links.push({
      type: 'markdown',
      text: match[1],
      url: match[2],
      line: content.substring(0, match.index).split('\n').length
    });
  }
  
  // Match raw URLs
  const urlRegex = /https?:\/\/[^\s\)"\']+/g;
  while ((match = urlRegex.exec(content)) !== null) {
    links.push({
      type: 'raw',
      text: null,
      url: match[0],
      line: content.substring(0, match.index).split('\n').length
    });
  }
  
  return links;
}

/**
 * Check if a URL is valid (not broken)
 * @param {string} url - URL to check
 * @returns {object} Result with status
 */
function checkUrl(url) {
  try {
    // Use curl to check the URL (faster than full HTTP request)
    const result = execSync(`curl -sI -o NUL -w "%{http_code}" --max-time 10 "${url}"`, {
      encoding: 'utf8',
      timeout: 15000,
      stdio: ['pipe', 'pipe', 'pipe']
    });
    
    const statusCode = parseInt(result.trim(), 10);
    return {
      url,
      status: statusCode,
      valid: statusCode >= 200 && statusCode < 400,
      error: null
    };
  } catch (error) {
    return {
      url,
      status: null,
      valid: false,
      error: error.message
    };
  }
}

/**
 * Check for broken links in documentation
 * @param {string} targetDir - Directory to scan
 * @param {object} options - Scan options
 * @returns {object} Check results
 */
function checkBrokenLinks(targetDir = process.cwd(), options = {}) {
  const results = {
    timestamp: new Date().toISOString(),
    target: targetDir,
    summary: {
      files_scanned: 0,
      links_found: 0,
      links_checked: 0,
      broken_links: 0,
      skipped_external: 0
    },
    files: [],
    broken: [],
    recommendations: []
  };

  const mdExtensions = ['.md', '.markdown', '.mdx'];
  const excludeDirs = ['node_modules', '.git', 'dist', 'build', '.next'];
  
  // Recursively find all markdown files
  function findMarkdownFiles(dir) {
    const files = [];
    
    try {
      const entries = fs.readdirSync(dir, { withFileTypes: true });
      
      for (const entry of entries) {
        const fullPath = path.join(dir, entry.name);
        
        if (entry.isDirectory()) {
          if (!excludeDirs.includes(entry.name)) {
            files.push(...findMarkdownFiles(fullPath));
          }
        } else if (entry.isFile()) {
          const ext = path.extname(entry.name).toLowerCase();
          if (mdExtensions.includes(ext)) {
            files.push(fullPath);
          }
        }
      }
    } catch (e) {
      // Skip inaccessible directories
    }
    
    return files;
  }

  const mdFiles = findMarkdownFiles(targetDir);
  results.summary.files_scanned = mdFiles.length;

  // Process each file
  for (const file of mdFiles) {
    try {
      const content = fs.readFileSync(file, 'utf8');
      const links = extractLinks(content);
      
      if (links.length === 0) continue;
      
      results.summary.links_found += links.length;
      
      const fileResult = {
        file: path.relative(targetDir, file),
        links: []
      };

      // Check each link
      for (const link of links) {
        // Skip anchor links and relative links
        if (link.url.startsWith('#') || link.url.startsWith('/') || link.url.startsWith('.')) {
          results.summary.skipped_external++;
          continue;
        }
        
        // Skip non-http links
        if (!link.url.startsWith('http://') && !link.url.startsWith('https://')) {
          continue;
        }
        
        results.summary.links_checked++;
        
        const checkResult = checkUrl(link.url);
        fileResult.links.push(checkResult);
        
        if (!checkResult.valid) {
          results.broken.push({
            file: path.relative(targetDir, file),
            line: link.line,
            url: link.url,
            status: checkResult.status,
            error: checkResult.error
          });
          results.summary.broken_links++;
        }
      }
      
      if (fileResult.links.length > 0) {
        results.files.push(fileResult);
      }
    } catch (e) {
      // Skip unreadable files
    }
  }

  // Generate recommendations
  if (results.summary.broken_links > 0) {
    results.recommendations.push(`Found ${results.summary.broken_links} broken link(s) - fix or remove them`);
  }
  if (results.summary.links_checked === 0) {
    results.recommendations.push('No external links found to check');
  }
  if (results.summary.broken_links === 0 && results.summary.links_checked > 0) {
    results.recommendations.push('All links are valid!');
  }
  
  return results;
}

/**
 * Format results for display
 * @param {object} results - Check results
 * @returns {string} Formatted output
 */
function formatResults(results) {
  const lines = [];

  lines.push('=== Broken Link Checker ===');
  lines.push(`Target: ${results.target}`);
  lines.push(`Time: ${results.timestamp}`);
  lines.push('');

  lines.push('Summary:');
  lines.push(`  Files scanned: ${results.summary.files_scanned}`);
  lines.push(`  Links found: ${results.summary.links_found}`);
  lines.push(`  Links checked: ${results.summary.links_checked}`);
  lines.push(`  Broken links: ${results.summary.broken_links}`);
  lines.push(`  Skipped: ${results.summary.skipped_external}`);
  lines.push('');

  if (results.broken.length > 0) {
    lines.push('Broken Links:');
    for (const link of results.broken.slice(0, 20)) { // Limit output
      lines.push(`  ${link.file}:${link.line}`);
      lines.push(`    URL: ${link.url}`);
      lines.push(`    Status: ${link.status || 'ERROR: ' + link.error}`);
    }
    if (results.broken.length > 20) {
      lines.push(`  ... and ${results.broken.length - 20} more`);
    }
    lines.push('');
  }

  if (results.recommendations.length > 0) {
    lines.push('Recommendations:');
    for (const rec of results.recommendations) {
      lines.push(`  - ${rec}`);
    }
  }

  return lines.join('\n');
}

/**
 * Main entry point
 */
function main() {
  const targetDir = process.argv[2] || process.cwd();
  const results = checkBrokenLinks(targetDir);
  console.log(formatResults(results));

  // Exit with error if broken links found
  if (results.summary.broken_links > 0) {
    process.exit(1);
  }
}

module.exports = {
  extractLinks,
  checkUrl,
  checkBrokenLinks,
  formatResults,
  main
};

// Run main if executed directly
if (require.main === module) {
  main();
}