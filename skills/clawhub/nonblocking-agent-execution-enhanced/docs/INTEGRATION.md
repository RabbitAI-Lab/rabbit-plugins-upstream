# 🔗 Integration Guide - Non-Blocking Agent Execution v2.0.0

This guide covers how to integrate the **nonblocking-agent-execution** skill into your applications, workflows, and systems.

---

## 📋 Table of Contents

1. [Quick Integration](#-quick-integration)
2. [Programmatic Usage](#-programmatic-usage)
3. [REST API Wrapper](#-rest-api-wrapper)
4. [Webhook Integration](#-webhook-integration)
5. [CI/CD Integration](#-cicd-integration)
6. [Monitoring Integration](#-monitoring-integration)
7. [Advanced Patterns](#-advanced-patterns)
8. [Troubleshooting](#-troubleshooting)

---

## 🚀 Quick Integration

### Option 1: Direct Usage (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/orionshaowswmw/nonblocking-agent-execution-enhanced.git
cd nonblocking-agent-execution-enhanced

# 2. Make executable
chmod +x scripts/jobctl.sh

# 3. Create directories
mkdir -p ~/.nonblocking/{run,logs,state,cache,feedback}

# 4. Use it!
./scripts/jobctl.sh start my-job 'your-command-here'
```

### Option 2: Install via Package Manager

```bash
# Install to a specific directory
npx --yes clawhub@latest install @orionshaowswmw/nonblocking-agent-execution \
  --workdir /opt/nonblocking \
  --dir /opt/nonblocking/skills

# Add to PATH
export PATH="/opt/nonblocking/skills/nonblocking-agent-execution/scripts:$PATH"

# Use it
jobctl.sh start my-job 'your-command'
```

### Option 3: Docker Container

```dockerfile
# Dockerfile
FROM ubuntu:24.04

# Install dependencies
RUN apt-get update && apt-get install -y bash curl python3 jq

# Copy skill files
COPY scripts/jobctl.sh /usr/local/bin/jobctl.sh
RUN chmod +x /usr/local/bin/jobctl.sh

# Create directories
RUN mkdir -p /data/nonblocking/{run,logs,state,cache,feedback}
ENV NONBLOCKING_BASE_DIR=/data/nonblocking

# Use it
CMD ["jobctl.sh", "start", "test-job", "echo hello"]
```

```bash
# Build and run
docker build -t nonblocking-agent .
docker run --rm nonblocking-agent
```

---

## 💻 Programmatic Usage

### Bash Script Integration

```bash
#!/bin/bash
# my_script.sh

# Source: my_script.sh

# Configure
JOB_ID="my-background-job"
COMMAND="long-running-task --param value"
CALLBACK_URL="https://my-api.com/callback"

# Start job
if ! ./scripts/jobctl.sh start "$JOB_ID" "$COMMAND" "$CALLBACK_URL" >/dev/null; then
    echo "Failed to start job"
    exit 1
fi

# Poll for completion
for i in {1..60}; do
    STATUS=$(./scripts/jobctl.sh status "$JOB_ID" | jq -r '.status')
    
    case "$STATUS" in
        completed|failed|stopped)
            echo "Job completed with status: $STATUS"
            break
            ;;
        running)
            echo "Job still running... ($i/60)"
            sleep 5
            ;;
        *)
            echo "Unknown status: $STATUS"
            sleep 5
            ;;
    esac
done

# Get output
OUTPUT=$(cat ~/.nonblocking/state/"$JOB_ID".output)
echo "Output: $OUTPUT"

# Cleanup
./scripts/jobctl.sh cleanup "$JOB_ID"
```

### Python Integration

```python
# my_app.py
import subprocess
import json
import time
from typing import Dict, Any

class NonBlockingExecutor:
    def __init__(self, jobctl_path: str = "./scripts/jobctl.sh"):
        self.jobctl_path = jobctl_path
    
    def start_job(
        self,
        job_id: str,
        command: str,
        callback_url: str = None,
        model: str = None,
        max_tokens: int = None
    ) -> Dict[str, Any]:
        """Start a non-blocking job."""
        cmd = [self.jobctl_path, "start", job_id, command]
        if callback_url:
            cmd.append(callback_url)
        if model:
            cmd.append(model)
        if max_tokens:
            cmd.append(str(max_tokens))
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Failed to start job: {result.stderr}")
        
        return json.loads(result.stdout)
    
    def get_status(self, job_id: str) -> Dict[str, Any]:
        """Get job status."""
        result = subprocess.run(
            [self.jobctl_path, "status", job_id],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise RuntimeError(f"Failed to get status: {result.stderr}")
        return json.loads(result.stdout)
    
    def poll_job(
        self,
        job_id: str,
        timeout: int = 30,
        interval: int = 2
    ) -> Dict[str, Any]:
        """Poll job until completion."""
        for i in range(timeout // interval):
            status = self.get_status(job_id)
            if status['status'] in ['completed', 'failed', 'stopped']:
                return status
            time.sleep(interval)
        
        raise TimeoutError(f"Job {job_id} did not complete in {timeout}s")
    
    def stop_job(self, job_id: str) -> Dict[str, Any]:
        """Stop a running job."""
        result = subprocess.run(
            [self.jobctl_path, "stop", job_id],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise RuntimeError(f"Failed to stop job: {result.stderr}")
        return json.loads(result.stdout)
    
    def cleanup_job(self, job_id: str) -> Dict[str, Any]:
        """Clean up job files."""
        result = subprocess.run(
            [self.jobctl_path, "cleanup", job_id],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise RuntimeError(f"Failed to cleanup job: {result.stderr}")
        return json.loads(result.stdout)


# Usage example
if __name__ == "__main__":
    executor = NonBlockingExecutor()
    
    # Start a job
    result = executor.start_job(
        job_id="python-job-1",
        command="python3 my_script.py --param value",
        callback_url="https://my-api.com/callback",
        model="gpt-4o-mini",
        max_tokens=2048
    )
    print(f"Started job: {result['job_id']}")
    
    # Poll for completion
    try:
        final_status = executor.poll_job("python-job-1", timeout=60)
        print(f"Job completed: {final_status['status']}")
    except TimeoutError as e:
        print(f"Timeout: {e}")
    
    # Cleanup
    executor.cleanup_job("python-job-1")
```

### Node.js Integration

```javascript
// myApp.js
const { execSync, exec } = require('child_process');
const path = require('path');

class NonBlockingExecutor {
    constructor(jobctlPath = path.join(__dirname, 'scripts', 'jobctl.sh')) {
        this.jobctlPath = jobctlPath;
    }
    
    startJob(jobId, command, callbackUrl = null, model = null, maxTokens = null) {
        let cmd = `${this.jobctlPath} start ${jobId} '${command}'`;
        if (callbackUrl) cmd += ` ${callbackUrl}`;
        if (model) cmd += ` ${model}`;
        if (maxTokens) cmd += ` ${maxTokens}`;
        
        try {
            const output = execSync(cmd, { encoding: 'utf8' });
            return JSON.parse(output);
        } catch (error) {
            throw new Error(`Failed to start job: ${error.stderr}`);
        }
    }
    
    getStatus(jobId) {
        try {
            const output = execSync(
                `${this.jobctlPath} status ${jobId}`,
                { encoding: 'utf8' }
            );
            return JSON.parse(output);
        } catch (error) {
            throw new Error(`Failed to get status: ${error.stderr}`);
        }
    }
    
    async pollJob(jobId, timeout = 30000, interval = 2000) {
        const startTime = Date.now();
        
        while (Date.now() - startTime < timeout) {
            const status = this.getStatus(jobId);
            if (['completed', 'failed', 'stopped'].includes(status.status)) {
                return status;
            }
            await new Promise(resolve => setTimeout(resolve, interval));
        }
        
        throw new Error(`Job ${jobId} did not complete in ${timeout}ms`);
    }
    
    stopJob(jobId) {
        try {
            const output = execSync(
                `${this.jobctlPath} stop ${jobId}`,
                { encoding: 'utf8' }
            );
            return JSON.parse(output);
        } catch (error) {
            throw new Error(`Failed to stop job: ${error.stderr}`);
        }
    }
    
    cleanupJob(jobId) {
        try {
            const output = execSync(
                `${this.jobctlPath} cleanup ${jobId}`,
                { encoding: 'utf8' }
            );
            return JSON.parse(output);
        } catch (error) {
            throw new Error(`Failed to cleanup job: ${error.stderr}`);
        }
    }
}

// Usage example
(async () => {
    const executor = new NonBlockingExecutor();
    
    // Start a job
    const result = executor.startJob(
        'node-job-1',
        'node myScript.js --param value',
        'https://my-api.com/callback',
        'gpt-4o-mini',
        2048
    );
    console.log(`Started job: ${result.job_id}`);
    
    // Poll for completion
    try {
        const finalStatus = await executor.pollJob('node-job-1');
        console.log(`Job completed: ${finalStatus.status}`);
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
    
    // Cleanup
    executor.cleanupJob('node-job-1');
})();
```

### Go Integration

```go
// main.go
package main

import (
	"encoding/json"
	"fmt"
	"os/exec"
	"strings"
)

type JobStatus struct {
	JobID      string `json:"job_id"`
	PID        int    `json:"pid"`
	Status     string `json:"status"`
	Message    string `json:"message"`
	StartTime  string `json:"start_time"`
	EndTime    string `json:"end_time"`
	ExitCode   int    `json:"exit_code"`
	CallbackURL string `json:"callback_url"`
	Model      string `json:"model"`
	MaxTokens  int    `json:"max_tokens"`
}

type NonBlockingExecutor struct {
	JobctlPath string
}

func NewNonBlockingExecutor(jobctlPath string) *NonBlockingExecutor {
	return &NonBlockingExecutor{JobctlPath: jobctlPath}
}

func (e *NonBlockingExecutor) StartJob(jobId, command, callbackUrl, model string, maxTokens int) (*JobStatus, error) {
	cmd := exec.Command(e.JobctlPath, "start", jobId, command)
	if callbackUrl != "" {
		cmd.Args = append(cmd.Args, callbackUrl)
	}
	if model != "" {
		cmd.Args = append(cmd.Args, model)
	}
	if maxTokens > 0 {
		cmd.Args = append(cmd.Args, fmt.Sprintf("%d", maxTokens))
	}
	
	output, err := cmd.Output()
	if err != nil {
		return nil, fmt.Errorf("failed to start job: %v", err)
	}
	
	var status JobStatus
	if err := json.Unmarshal(output, &status); err != nil {
		return nil, fmt.Errorf("failed to parse output: %v", err)
	}
	
	return &status, nil
}

func (e *NonBlockingExecutor) GetStatus(jobId string) (*JobStatus, error) {
	cmd := exec.Command(e.JobctlPath, "status", jobId)
	output, err := cmd.Output()
	if err != nil {
		return nil, fmt.Errorf("failed to get status: %v", err)
	}
	
	var status JobStatus
	if err := json.Unmarshal(output, &status); err != nil {
		return nil, fmt.Errorf("failed to parse output: %v", err)
	}
	
	return &status, nil
}

func main() {
	executor := NewNonBlockingExecutor("./scripts/jobctl.sh")
	
	// Start a job
	status, err := executor.StartJob(
		"go-job-1",
		"echo 'Hello from Go'",
		"https://my-api.com/callback",
		"gpt-4o-mini",
		2048,
	)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	
	fmt.Printf("Started job: %s with PID: %d\n", status.JobID, status.PID)
	
	// Get status
	status, err = executor.GetStatus("go-job-1")
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	
	fmt.Printf("Job status: %s\n", status.Status)
}
```

---

## 🌐 REST API Wrapper

Create a simple HTTP server that wraps jobctl.sh for remote access.

### Python Flask API

```python
# api.py
from flask import Flask, request, jsonify
import subprocess
import json
import os

app = Flask(__name__)
JOBCTL_PATH = "./scripts/jobctl.sh"

@app.route('/jobs', methods=['POST'])
def create_job():
    data = request.json
    job_id = data.get('job_id')
    command = data.get('command')
    callback_url = data.get('callback_url')
    model = data.get('model')
    max_tokens = data.get('max_tokens')
    
    if not job_id or not command:
        return jsonify({'error': 'job_id and command are required'}), 400
    
    cmd = [JOBCTL_PATH, 'start', job_id, command]
    if callback_url:
        cmd.append(callback_url)
    if model:
        cmd.append(model)
    if max_tokens:
        cmd.append(str(max_tokens))
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return jsonify(json.loads(result.stdout)), 202
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.stderr}), 500

@app.route('/jobs/<job_id>', methods=['GET'])
def get_job(job_id):
    cmd = [JOBCTL_PATH, 'status', job_id]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return jsonify(json.loads(result.stdout)), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.stderr}), 404

@app.route('/jobs/<job_id>/stop', methods=['POST'])
def stop_job(job_id):
    cmd = [JOBCTL_PATH, 'stop', job_id]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return jsonify(json.loads(result.stdout)), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.stderr}), 404

@app.route('/jobs/<job_id>/log', methods=['GET'])
def get_log(job_id):
    lines = request.args.get('lines', '50')
    cmd = [JOBCTL_PATH, 'log', job_id, lines]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout, 200, {'Content-Type': 'text/plain'}
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.stderr}), 404

@app.route('/jobs/<job_id>/cleanup', methods=['POST'])
def cleanup_job(job_id):
    cmd = [JOBCTL_PATH, 'cleanup', job_id]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return jsonify(json.loads(result.stdout)), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.stderr}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
```

### Usage

```bash
# Start the API server
python3 api.py &

# Create a job via API
curl -X POST http://localhost:8080/jobs \
  -H "Content-Type: application/json" \
  -d '{
    "job_id": "api-job-1",
    "command": "echo hello from API",
    "callback_url": "https://my-callback.com",
    "model": "gpt-4o-mini",
    "max_tokens": 2048
  }'

# Check job status
curl http://localhost:8080/jobs/api-job-1

# Stop a job
curl -X POST http://localhost:8080/jobs/api-job-1/stop

# Get logs
curl http://localhost:8080/jobs/api-job-1/log?lines=100

# Cleanup
curl -X POST http://localhost:8080/jobs/api-job-1/cleanup
```

---

## 📡 Webhook Integration

### Receiving Callbacks

When a job completes, it can POST results to a callback URL. Here's how to handle it.

#### Python Flask Callback Handler

```python
# callback_server.py
from flask import Flask, request, jsonify
import json
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/callback', methods=['POST'])
def handle_callback():
    data = request.json
    logger.info(f"Received callback: {json.dumps(data, indent=2)}")
    
    # Process the callback
    job_id = data.get('job_id')
    status = data.get('status')
    exit_code = data.get('exit_code')
    output = data.get('output')
    
    # Your business logic here
    if status == 'completed':
        logger.info(f"Job {job_id} completed successfully")
        # Process output
        process_output(job_id, output)
    elif status == 'failed':
        logger.error(f"Job {job_id} failed with exit code {exit_code}")
        # Handle failure
        handle_failure(job_id, exit_code, data.get('error_message'))
    elif status == 'stopped':
        logger.warning(f"Job {job_id} was stopped")
        # Handle stopped job
        handle_stopped(job_id)
    
    return jsonify({'status': 'received', 'job_id': job_id}), 200

def process_output(job_id, output):
    """Process job output."""
    # Implement your output processing logic
    print(f"Processing output from {job_id}: {output[:100]}...")
    # Save to database, trigger next steps, etc.

def handle_failure(job_id, exit_code, error_message):
    """Handle job failure."""
    # Implement your failure handling logic
    print(f"Job {job_id} failed: {error_message}")
    # Retry, alert, etc.

def handle_stopped(job_id):
    """Handle stopped job."""
    # Implement your stopped job handling logic
    print(f"Job {job_id} was stopped")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```

### Testing Callbacks Locally

Use a tool like [webhook.site](https://webhook.site) or [ngrok](https://ngrok.com) for testing.

```bash
# Start ngrok to expose local server
ngrok http 8000

# Start callback server
python3 callback_server.py &

# Start a job with callback
./scripts/jobctl.sh start callback-test 'echo hello' http://your-ngrok-url.ngrok.io/callback
```

---

## 🔄 CI/CD Integration

### GitHub Actions

```yaml
# .github/workflows/nonblocking-jobs.yml
name: Non-Blocking Jobs

on:
  workflow_dispatch:
  push:
    branches: [ main ]

jobs:
  run-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up nonblocking-agent-execution
        run: |
          git clone https://github.com/orionshaowswmw/nonblocking-agent-execution-enhanced.git
          cd nonblocking-agent-execution-enhanced
          chmod +x scripts/jobctl.sh
          mkdir -p ~/.nonblocking/{run,logs,state,cache,feedback}
      
      - name: Run long build in background
        run: |
          cd nonblocking-agent-execution-enhanced
          ./scripts/jobctl.sh start ci-build 'npm install && npm run build' 
            https://api.github.com/repos/${{ github.repository }}/dispatches 
            gpt-4o-mini 4096
      
      - name: Poll for completion
        run: |
          cd nonblocking-agent-execution-enhanced
          for i in {1..60}; do
            STATUS=$(./scripts/jobctl.sh status ci-build | jq -r '.status')
            if [[ "$STATUS" == "completed" ]]; then
              echo "Build completed!"
              ./scripts/jobctl.sh log ci-build 100
              exit 0
            fi
            sleep 10
          done
          echo "Build timed out"
          exit 1
      
      - name: Cleanup
        if: always()
        run: |
          cd nonblocking-agent-execution-enhanced
          ./scripts/jobctl.sh cleanup ci-build || true
```

### GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - deploy

nonblocking-build:
  stage: build
  script:
    - git clone https://github.com/orionshaowswmw/nonblocking-agent-execution-enhanced.git
    - cd nonblocking-agent-execution-enhanced
    - chmod +x scripts/jobctl.sh
    - mkdir -p ~/.nonblocking/{run,logs,state,cache,feedback}
    - ./scripts/jobctl.sh start gitlab-build 'make build' $CI_API_V4_URL/projects/$CI_PROJECT_ID/pipeline 
    - |
      for i in {1..60}; do
        STATUS=$(./scripts/jobctl.sh status gitlab-build | jq -r '.status')
        if [[ "$STATUS" == "completed" ]]; then
          echo "Build completed!"
          ./scripts/jobctl.sh log gitlab-build 100
          exit 0
        fi
        sleep 10
      done
      echo "Build timed out"
      exit 1
  after_script:
    - cd nonblocking-agent-execution-enhanced
    - ./scripts/jobctl.sh cleanup gitlab-build || true
```

---

## 📊 Monitoring Integration

### Prometheus Metrics

Create a metrics exporter for Prometheus.

```python
# metrics_exporter.py
from prometheus_client import start_http_server, Gauge, Counter
import subprocess
import json
import time
import os

# Metrics
JOB_STATUS = Gauge('nonblocking_job_status', 'Job status', ['job_id', 'status'])
JOB_DURATION = Gauge('nonblocking_job_duration_seconds', 'Job duration in seconds', ['job_id'])
JOB_TOKENS = Gauge('nonblocking_job_tokens_used', 'Tokens used by job', ['job_id'])
JOB_TOKEN_RATE = Gauge('nonblocking_job_token_rate', 'Token rate per second', ['job_id'])
JOB_COUNT = Counter('nonblocking_job_count_total', 'Total jobs', ['status'])
JOB_QUEUE = Gauge('nonblocking_job_queue_size', 'Number of queued jobs')

STATE_DIR = os.getenv('NONBLOCKING_BASE_DIR', '~/.nonblocking') + '/state'

def collect_metrics():
    """Collect metrics from all job state files."""
    # Reset gauges
    JOB_STATUS.reset()
    JOB_DURATION.reset()
    JOB_TOKENS.reset()
    JOB_TOKEN_RATE.reset()
    
    # Count jobs by status
    status_counts = {'queued': 0, 'running': 0, 'completed': 0, 'failed': 0, 'stopped': 0}
    
    # Process each job
    for filename in os.listdir(STATE_DIR):
        if not filename.endswith('.json'):
            continue
        
        job_id = filename[:-5]  # Remove .json
        filepath = os.path.join(STATE_DIR, filename)
        
        try:
            with open(filepath, 'r') as f:
                state = json.load(f)
            
            status = state.get('status', 'unknown')
            status_counts[status] = status_counts.get(status, 0) + 1
            
            # Set status gauge
            JOB_STATUS.labels(job_id=job_id, status=status).set(1)
            
            # Set duration if available
            start_time = state.get('start_time')
            end_time = state.get('end_time')
            if start_time and end_time:
                # Parse ISO timestamps
                from datetime import datetime
                start = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
                end = datetime.fromisoformat(end_time.replace('Z', '+00:00'))
                duration = (end - start).total_seconds()
                JOB_DURATION.labels(job_id=job_id).set(duration)
            
            # Set token metrics
            tokens_used = state.get('tokens_used', 0)
            token_rate = state.get('token_rate', 0)
            JOB_TOKENS.labels(job_id=job_id).set(tokens_used)
            JOB_TOKEN_RATE.labels(job_id=job_id).set(token_rate)
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    
    # Update counters
    for status, count in status_counts.items():
        JOB_COUNT.labels(status=status).inc(count)
    
    # Update queue size
    JOB_QUEUE.set(status_counts.get('queued', 0))

if __name__ == '__main__':
    # Start metrics server
    start_http_server(8000)
    
    # Collect metrics every 10 seconds
    while True:
        collect_metrics()
        time.sleep(10)
```

### Grafana Dashboard

Create a Grafana dashboard with panels for:
- Job status distribution
- Running jobs count
- Completed jobs rate
- Failed jobs rate
- Token usage per job
- Average token rate
- Job duration distribution

---

## 🎯 Advanced Patterns

### 1. Job Chaining

```bash
# Start first job
./scripts/jobctl.sh start job1 'step1' 

# Wait for job1 to complete
while true; do
    STATUS=$(./scripts/jobctl.sh status job1 | jq -r '.status')
    if [[ "$STATUS" == "completed" ]]; then
        break
    fi
    sleep 5
done

# Start second job that depends on first
./scripts/jobctl.sh start job2 'step2 --input $(cat ~/.nonblocking/state/job1.output)'
```

### 2. Parallel Job Execution

```bash
# Start multiple independent jobs
for i in {1..5}; do
    ./scripts/jobctl.sh start parallel-job-$i "process_item $i" https://callback.url
done

# Monitor all jobs
watch -n 2 './scripts/jobctl.sh list'

# Wait for all to complete
while true; do
    RUNNING=$(./scripts/jobctl.sh list running | wc -l)
    if [[ "$RUNNING" -eq 0 ]]; then
        echo "All jobs completed!"
        break
    fi
    sleep 10
done
```

### 3. Retry with Exponential Backoff

```bash
MAX_RETRIES=3
RETRY_DELAY=5

for attempt in $(seq 1 $MAX_RETRIES); do
    ./scripts/jobctl.sh start retry-job-$attempt 'flaky-command' >/dev/null 2>&1
    
    # Wait a bit
    sleep $RETRY_DELAY
    
    # Check if successful
    STATUS=$(./scripts/jobctl.sh status retry-job-$attempt | jq -r '.status')
    if [[ "$STATUS" == "completed" ]]; then
        echo "Success on attempt $attempt"
        break
    fi
    
    # Cleanup failed attempt
    ./scripts/jobctl.sh cleanup retry-job-$attempt >/dev/null 2>&1
    
    # Exponential backoff
    RETRY_DELAY=$((RETRY_DELAY * 2))
done
```

### 4. Token-Aware Job Execution

```bash
# Set token thresholds
TOKEN_WARNING_THRESHOLD=3000
TOKEN_ERROR_THRESHOLD=5000

# Start job with token monitoring
./scripts/jobctl.sh start token-monitor-job 'complex-command' https://callback.url

# Monitor token usage
while true; do
    STATUS=$(./scripts/jobctl.sh status token-monitor-job)
    TOKENS=$(echo "$STATUS" | jq -r '.tokens_used')
    
    if [[ "$TOKENS" -gt "$TOKEN_ERROR_THRESHOLD" ]]; then
        echo "Error: Token usage exceeded threshold!"
        ./scripts/jobctl.sh stop token-monitor-job
        break
    elif [[ "$TOKENS" -gt "$TOKEN_WARNING_THRESHOLD" ]]; then
        echo "Warning: Token usage approaching threshold"
    fi
    
    # Check job status
    JOB_STATUS=$(echo "$STATUS" | jq -r '.status')
    if [[ "$JOB_STATUS" == "completed" ]]; then
        echo "Job completed with $TOKENS tokens used"
        break
    fi
    
    sleep 10
done
```

### 5. Self-Improving Workflow

```bash
# Start a job
./scripts/jobctl.sh start improve-job 'generate-report' https://callback.url

# Wait for completion
./scripts/jobctl.sh poll improve-job 30

# Get output
OUTPUT=$(cat ~/.nonblocking/state/improve-job.output)

# Verify output
./scripts/jobctl.sh verify improve-job

# Record feedback (simulating user feedback)
echo '{"feedback":"Report was helpful but could be more detailed", "rating":4}' > \
  ~/.nonblocking/feedback/improve-job.feedback

# Next job benefits from previous feedback
./scripts/jobctl.sh start improve-job-2 'generate-report --verbose' https://callback.url
```

---

## 🐞 Troubleshooting

### Common Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| **Permission denied** | `Permission denied` errors | Run with appropriate permissions, check file permissions |
| **Command not found** | `command not found` | Ensure command is in PATH or use full path |
| **Job hangs** | Job stays in "running" status | Check logs with `./scripts/jobctl.sh log <job_id>` |
| **High token usage** | Token warnings in logs | Optimize command, reduce output size |
| **Verification failed** | Low verification score | Check output for hallucinations, fix command |
| **Callback failed** | No callback received | Verify callback URL, check network/firewall |
| **Watchdog timeout** | Job killed by watchdog | Increase `MAX_RUNTIME` or optimize command |

### Debugging Steps

1. **Check job status**
   ```bash
   ./scripts/jobctl.sh status <job_id>
   ```

2. **Review logs**
   ```bash
   ./scripts/jobctl.sh log <job_id> 100
   ```

3. **Get debug info**
   ```bash
   ./scripts/jobctl.sh debug <job_id>
   ```

4. **Enable debug mode**
   ```bash
   LOG_LEVEL=DEBUG ./scripts/jobctl.sh start <job_id> '<command>'
   ```

5. **Check environment**
   ```bash
   echo "NONBLOCKING_BASE_DIR: $NONBLOCKING_BASE_DIR"
   echo "MAX_RUNTIME: $MAX_RUNTIME"
   echo "POLL_INTERVAL: $POLL_INTERVAL"
   ```

6. **Verify directories**
   ```bash
   ls -la ~/.nonblocking/
   ls -la ~/.nonblocking/run/
   ls -la ~/.nonblocking/logs/
   ls -la ~/.nonblocking/state/
   ```

### Performance Tuning

Adjust these environment variables for optimal performance:

```bash
# Increase timeout for long jobs
export MAX_RUNTIME=3600  # 1 hour

# Reduce polling interval for faster response
export POLL_INTERVAL=1

# Increase max poll attempts
export MAX_POLL_ATTEMPTS=300

# Set token thresholds
export TOKEN_WARNING_THRESHOLD=3000
export TOKEN_ERROR_THRESHOLD=6000

# Change base directory
export NONBLOCKING_BASE_DIR=/var/lib/nonblocking

# Enable debug logging
export LOG_LEVEL=DEBUG
```

---

## 📖 Additional Resources

- [SKILL.md](../SKILL.md) - Complete skill documentation
- [README.md](../README.md) - Quick start guide
- [BEST_PRACTICES.md](./BEST_PRACTICES.md) - Best practices guide
- [API.md](./API.md) - API documentation

---

**Happy Integrating! 🚀**

For issues, questions, or contributions, please refer to the main [README](../README.md).
