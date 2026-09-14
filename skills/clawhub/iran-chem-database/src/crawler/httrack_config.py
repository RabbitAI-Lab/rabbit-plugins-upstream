"""HTTrackMirrorConfig — dataclass for one mirror job (spec §3.1)."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

HTTRACK_BASE_DIR = "/var/lib/iran_chem_db/mirrors"

DEFAULT_INCLUDE_FILTERS = [
    "+*.html", "+*.htm", "+*.php", "+*.asp", "+*.aspx",
    "+*.jsp", "+*.pdf", "+*.xlsx", "+*.xls", "+*.csv",
    "+*.doc", "+*.docx",
]
DEFAULT_EXCLUDE_FILTERS = [
    "-*.jpg", "-*.jpeg", "-*.png", "-*.gif", "-*.svg",
    "-*.mp4", "-*.mp3", "-*.avi", "-*.mov",
    "-*.zip", "-*.rar", "-*.tar.gz",
    "-*.css", "-*.woff", "-*.woff2", "-*.ttf", "-*.eot",
    "-ad.doubleclick.net/*",
    "-*.google-analytics.com/*",
]


@dataclass
class HTTrackMirrorConfig:
    """Configuration for a single HTTrack mirror job."""

    supplier_id: int
    project_name: str
    urls: List[str]
    output_dir: str
    depth: int = 5
    ext_depth: int = 0
    max_rate: int = 25000
    connections_per_second: float = 2.0
    sockets: int = 4
    max_time: int = 7200
    max_size: int = 0
    robots_txt: int = 2
    include_filters: List[str] = field(default_factory=lambda: list(DEFAULT_INCLUDE_FILTERS))
    exclude_filters: List[str] = field(default_factory=lambda: list(DEFAULT_EXCLUDE_FILTERS))
    user_agent: str = "IranChemDB/1.0 (Research Chemical Database Crawler; contact@iranchem.db)"
    proxy: Optional[str] = None
    extra_flags: List[str] = field(default_factory=list)
    assume_types: str = "asp=text/html,php=text/html,aspx=text/html"
    stay_on_same_domain: bool = True
    detect_changes: bool = True

    def to_flags(self, update: bool = False) -> List[str]:
        """Build the httrack CLI argument list from this config."""
        cmd: List[str] = ["httrack"]
        if update:
            cmd += ["--update", "-O", self.output_dir]
        else:
            cmd += list(self.urls) + ["-O", self.output_dir]
            cmd += [
                f"--depth={self.depth}",
                f"--ext-depth={self.ext_depth}",
                f"--max-rate={self.max_rate}",
                f"--connection-per-second={self.connections_per_second}",
                f"--sockets={self.sockets}",
            ]
            if self.max_time > 0:
                cmd += [f"--max-time={self.max_time}"]
            if self.max_size > 0:
                cmd += [f"--max-size={self.max_size}"]
            cmd += [f"--robots={self.robots_txt}", "-F", self.user_agent]
            if self.stay_on_same_domain:
                cmd.append("--stay-on-same-domain")
            if self.assume_types:
                cmd += ["--assume", self.assume_types]
            if self.proxy:
                cmd += ["-P", self.proxy]
            cmd += self.include_filters + self.exclude_filters
        # NOTE: change detection needs no special flag. HTTrack always writes its
        # change artifacts into hts-cache/ (new.lst, new.txt) during --update runs;
        # the engine reads those (and hts-changes.json when present) after the run.
        cmd += ["-q", "--do-not-log"]
        cmd += self.extra_flags
        return cmd
