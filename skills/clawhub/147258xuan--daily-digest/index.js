const fs = require('fs');
const path = require('path');

const workspaceRoot = process.env.WORKSPACE_ROOT || process.cwd();
const memoryDir = path.join(workspaceRoot, 'memory');

function getRecentMemoryFiles(days = 1) {
  const files = [];
  const now = new Date();
  
  for (let i = 0; i < days; i++) {
    const date = new Date(now);
    date.setDate(date.getDate() - i);
    const dateStr = date.toISOString().split('T')[0];
    const filePath = path.join(memoryDir, `${dateStr}.md`);
    
    if (fs.existsSync(filePath)) {
      files.push({
        date: dateStr,
        path: filePath,
        content: fs.readFileSync(filePath, 'utf8')
      });
    }
  }
  
  return files;
}

function getEvolutionState() {
  const statePath = path.join(workspaceRoot, 'memory', 'evolution', 'evolution_state.json');
  
  if (!fs.existsSync(statePath)) {
    return null;
  }
  
  try {
    return JSON.parse(fs.readFileSync(statePath, 'utf8'));
  } catch {
    return null;
  }
}

function generateDigest(options = {}) {
  const days = options.days || 1;
  const memoryFiles = getRecentMemoryFiles(days);
  const evolutionState = getEvolutionState();
  
  const lines = [];
  lines.push(`# Daily Digest`);
  lines.push(`\nGenerated: ${new Date().toISOString()}\n`);
  
  if (memoryFiles.length === 0) {
    lines.push('No memory files found for the specified period.\n');
  } else {
    lines.push(`## Recent Memory (${memoryFiles.length} file(s))\n`);
    
    for (const file of memoryFiles) {
      lines.push(`### ${file.date}\n`);
      const preview = file.content.slice(0, 500);
      lines.push(preview);
      if (file.content.length > 500) {
        lines.push(`\n... (truncated, ${file.content.length} bytes total)\n`);
      }
      lines.push('');
    }
  }
  
  if (evolutionState) {
    lines.push(`## Evolution State\n`);
    lines.push(`- Total cycles: ${evolutionState.cycleCount || 0}`);
    lines.push(`- Status: ${evolutionState.status || 'unknown'}`);
    
    if (evolutionState.last_cycle) {
      lines.push(`- Last cycle: #${evolutionState.last_cycle.id || '?'}`);
      lines.push(`- Last gene: ${evolutionState.last_cycle.gene || 'unknown'}`);
      lines.push(`- Last outcome: ${evolutionState.last_cycle.outcome || 'unknown'}`);
    }
    
    lines.push('');
  }
  
  return lines.join('\n');
}

module.exports = {
  generateDigest,
  getRecentMemoryFiles,
  getEvolutionState
};
