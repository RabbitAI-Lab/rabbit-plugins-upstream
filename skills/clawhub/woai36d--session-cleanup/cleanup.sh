#!/usr/bin/env bash
#
# session-cleanup.sh - Lightweight OpenClaw session cleanup
# Usage: cleanup.sh [--dry-run] [--backup-days N] [--trajectory-days N] [--report]

set -euo pipefail

# Config
AGENT_ID="${AGENT_ID:-main}"
SESSION_DIR="${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/agents/$AGENT_ID/sessions"
TRASH_DIR="${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/.trash/sessions"
LOG_DIR="${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs"
LOG_FILE="$LOG_DIR/session-cleanup.log"

# Defaults
BACKUP_DAYS=7
TRAJECTORY_DAYS=3
LOCK_DAYS=1
DRY_RUN=false
REPORT_ONLY=false

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

usage() {
    echo "Usage: $(basename "$0") [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --dry-run              Preview deletions without executing"
    echo "  --backup-days N        Retain backup files for N days (default: 7)"
    echo "  --trajectory-days N    Retain trajectory files for N days (default: 3)"
    echo "  --report               Show disk usage report only"
    echo "  --help                 Show this help"
    echo ""
    echo "Examples:"
    echo "  $(basename "$0") --dry-run"
    echo "  $(basename "$0") --backup-days 3 --trajectory-days 1"
    exit 0
}

log() {
    local msg="[$(date '+%Y-%m-%d %H:%M:%S')] $1"
    echo "$msg" >> "$LOG_FILE" 2>/dev/null || true
}

parse_args() {
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --dry-run) DRY_RUN=true ;;
            --backup-days) BACKUP_DAYS="$2"; shift ;;
            --trajectory-days) TRAJECTORY_DAYS="$2"; shift ;;
            --report) REPORT_ONLY=true ;;
            --help) usage ;;
            *) echo "Unknown option: $1"; usage ;;
        esac
        shift
    done
}

ensure_dirs() {
    mkdir -p "$TRASH_DIR" "$LOG_DIR"
}

# Check if a file belongs to an active session
is_active_session() {
    local file="$1"
    local basename_file
    basename_file=$(basename "$file")
    
    # Extract session ID (first 36 chars of UUID)
    local session_id
    session_id=$(echo "$basename_file" | grep -oE '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}' || true)
    
    [[ -z "$session_id" ]] && return 1
    
    # Check if there's a .jsonl.lock file for this session
    if [[ -f "$SESSION_DIR/${session_id}.jsonl.lock" ]]; then
        return 0
    fi
    
    # Check if the main .jsonl was modified in the last hour
    local main_jsonl="$SESSION_DIR/${session_id}.jsonl"
    if [[ -f "$main_jsonl" ]]; then
        local mtime
        mtime=$(stat -f %m "$main_jsonl" 2>/dev/null || stat -c %Y "$main_jsonl" 2>/dev/null || echo 0)
        local now
        now=$(date +%s)
        if (( now - mtime < 3600 )); then
            return 0
        fi
    fi
    
    return 1
}

# Move file to trash (or simulate)
move_to_trash() {
    local file="$1"
    local basename_file
    basename_file=$(basename "$file")
    
    if [[ "$DRY_RUN" == true ]]; then
        echo -e "${YELLOW}[DRY-RUN] Would move: $basename_file${NC}"
        return
    fi
    
    # Create dated trash subdir
    local trash_subdir="$TRASH_DIR/$(date +%Y%m%d)"
    mkdir -p "$trash_subdir"
    
    mv "$file" "$trash_subdir/$basename_file" 2>/dev/null || {
        echo -e "${RED}Failed to move: $basename_file${NC}"
        return 1
    }
    
    echo -e "${GREEN}✓ Moved to trash: $basename_file${NC}"
    log "MOVED: $file -> $trash_subdir/$basename_file"
}

clean_pattern() {
    local pattern="$1"
    local days="$2"
    local description="$3"
    local count=0
    local total_size=0
    
    log "Scanning: $description (older than $days days)"
    
    while IFS= read -r file; do
        [[ -z "$file" ]] && continue
        
        # Skip active sessions
        if is_active_session "$file"; then
            echo -e "${YELLOW}⊘ Skipped (active): $(basename "$file")${NC}"
            continue
        fi
        
        local size
        size=$(stat -f %z "$file" 2>/dev/null || stat -c %s "$file" 2>/dev/null || echo 0)
        total_size=$((total_size + size))
        count=$((count + 1))
        
        move_to_trash "$file"
    done < <(find "$SESSION_DIR" -maxdepth 1 -name "$pattern" -mtime +"$days" 2>/dev/null)
    
    if [[ "$count" -gt 0 ]]; then
        local human_size
        human_size=$(numfmt --to=iec "$total_size" 2>/dev/null || echo "${total_size}B")
        log "CLEANED: $count files ($human_size) - $description"
    else
        log "None found: $description"
    fi
    
    # Return count (max 255 due to exit code limits)
    if [[ "$count" -gt 255 ]]; then
        return 255
    fi
    return $count
}

show_report() {
    echo ""
    echo "📊 Session Directory Report"
    echo "========================="
    echo "Directory: $SESSION_DIR"
    echo ""
    
    # Total size
    local total
    total=$(du -sh "$SESSION_DIR" 2>/dev/null | cut -f1)
    echo "Total size: $total"
    echo ""
    
    # Breakdown by file type
    echo "Breakdown by type:"
    for pattern in "*.jsonl" "*.jsonl.reset.*" "*.checkpoint.*" "*.trajectory.jsonl" "*.trajectory-path.json" "*.jsonl.lock"; do
        local size
        size=$(find "$SESSION_DIR" -maxdepth 1 -name "$pattern" -exec du -ch {} + 2>/dev/null | grep total | cut -f1)
        local count
        count=$(find "$SESSION_DIR" -maxdepth 1 -name "$pattern" 2>/dev/null | wc -l | tr -d ' ')
        if [[ -n "$size" && "$size" != "0B" ]]; then
            printf "  %-30s %6s (%s files)\n" "$pattern" "$size" "$count"
        fi
    done
    echo ""
    
    # Largest files
    echo "Top 5 largest files:"
    find "$SESSION_DIR" -maxdepth 1 -type f -exec ls -lh {} + 2>/dev/null | \
        sort -k5 -rh | head -5 | \
        awk '{printf "  %-10s %s\n", $5, $9}'
    echo ""
    
    # Active sessions
    local active_count
    active_count=$(find "$SESSION_DIR" -maxdepth 1 -name "*.jsonl.lock" 2>/dev/null | wc -l | tr -d ' ')
    echo "Active sessions (locked): $active_count"
    echo ""
}

main() {
    parse_args "$@"
    ensure_dirs
    
    if [[ ! -d "$SESSION_DIR" ]]; then
        echo "Error: Session directory not found: $SESSION_DIR"
        exit 1
    fi
    
    log "=== Session Cleanup Started ==="
    log "Config: backups=${BACKUP_DAYS}d, trajectories=${TRAJECTORY_DAYS}d, locks=${LOCK_DAYS}d, dry-run=$DRY_RUN"
    
    if [[ "$REPORT_ONLY" == true ]]; then
        show_report
        exit 0
    fi
    
    show_report
    
    if [[ "$DRY_RUN" == true ]]; then
        echo -e "\n${YELLOW}🔍 DRY RUN MODE - No files will be deleted${NC}\n"
    else
        echo -e "\n${YELLOW}⚠️  Starting cleanup in 3 seconds... (Ctrl+C to cancel)${NC}"
        sleep 3
    fi
    
    # Clean each pattern
    local total_cleaned=0
    clean_pattern "*.jsonl.reset.*" "$BACKUP_DAYS" "Session reset backups"
    total_cleaned=$((total_cleaned + $?))
    clean_pattern "*.checkpoint.*.jsonl" "$BACKUP_DAYS" "Checkpoint files"
    total_cleaned=$((total_cleaned + $?))
    clean_pattern "*.trajectory.jsonl" "$TRAJECTORY_DAYS" "Trajectory logs"
    total_cleaned=$((total_cleaned + $?))
    clean_pattern "*.trajectory-path.json" "$TRAJECTORY_DAYS" "Trajectory indexes"
    total_cleaned=$((total_cleaned + $?))
    clean_pattern "*.jsonl.lock" "$LOCK_DAYS" "Stale lock files"
    total_cleaned=$((total_cleaned + $?))
    
    # Summary
    echo ""
    if [[ "$total_cleaned" -gt 0 ]]; then
        echo "✅ Cleanup complete ($total_cleaned patterns had files to clean)"
    else
        echo "✅ Cleanup complete (nothing to clean)"
    fi
    
    # Show new totals
    local new_total
    new_total=$(du -sh "$SESSION_DIR" 2>/dev/null | cut -f1)
    echo "New total size: $new_total"
    
    log "=== Session Cleanup Complete ==="
    log "New total size: $new_total"
    echo ""
    echo "Trashed files are in: $TRASH_DIR"
    echo "Logs: $LOG_FILE"
}

main "$@"
