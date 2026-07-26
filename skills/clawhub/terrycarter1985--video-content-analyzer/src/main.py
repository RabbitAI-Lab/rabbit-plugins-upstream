#!/usr/bin/env python3
"""
Video Content Analysis & Documentation Workflow
Integrates video frame extraction, web search, database storage, and wiki publishing
"""
import os
import uuid
from dotenv import load_dotenv
from modules.video_processor import VideoProcessor
from modules.search_client import SearchClient
from modules.database_client import DatabaseClient
from modules.feishu_wiki_client import FeishuWikiClient
from modules.batch_processor import BatchProcessor

# Load environment variables
load_dotenv()

class VideoAnalyzer:
    def __init__(self):
        self.video_processor = VideoProcessor()
        self.search_client = SearchClient()
        self.db_client = DatabaseClient()
        self.wiki_client = FeishuWikiClient()
        
        self.frames_output_dir = os.getenv("FRAMES_OUTPUT_DIR", "./extracted_frames")
        os.makedirs(self.frames_output_dir, exist_ok=True)
    
    def process_video(self, video_path: str, user_id: str, space_id: str,
                      parent_node_token: str = None, category: str = None,
                      batch_id: str = None) -> dict:
        """
        Full video processing workflow:
        1. Extract keyframes
        2. Store metadata in database
        3. Search for frame content information
        4. Generate wiki page with findings
        5. Publish to Feishu Wiki

        When called from a batch run, `parent_node_token` groups the generated
        page under a category node, `category` is persisted on the wiki record,
        and `batch_id` links the video asset back to its batch.
        """
        video_filename = os.path.basename(video_path)
        file_size = os.path.getsize(video_path)
        
        # Step 1: Get video info and save to database
        video_info = self.video_processor.get_video_info(video_path)
        video_id = self.db_client.save_video_asset(
            user_id=user_id,
            filename=video_filename,
            storage_path=video_path,
            duration=video_info.duration_seconds,
            file_size=file_size,
            batch_id=batch_id
        )
        
        print(f"Created video record: {video_id}")
        
        # Step 2: Extract keyframes
        print(f"Extracting keyframes from {video_filename}...")
        frames = self.video_processor.extract_keyframes(video_path, interval_seconds=10)
        print(f"Extracted {len(frames)} frames")
        
        # Step 3: Process each frame
        processed_frames = []
        frame_ids = []
        
        for i, frame in enumerate(frames):
            print(f"Processing frame {i+1}/{len(frames)}...")
            
            # Save frame to storage
            frame_filename = f"{video_id}_frame_{frame.frame_number:06d}.jpg"
            frame_path = os.path.join(self.frames_output_dir, frame_filename)
            self.video_processor.save_frame(frame, frame_path)
            
            # Save frame record to database
            frame_id = self.db_client.save_frame(
                video_id=video_id,
                frame_number=frame.frame_number,
                timestamp=frame.timestamp_seconds,
                storage_path=frame_path,
                width=frame.width,
                height=frame.height,
                content_tags=[]  # Would be populated by OCR/vision model in production
            )
            frame_ids.append(frame_id)
            
            # Step 4: Search for related information (using mock query for demo)
            # In production, this would use OCR/vision model output as search query
            search_query = f"reference information for frame content"
            search_results = self.search_client.search_image_content(search_query, num_results=3)
            
            # Save search results
            self.db_client.save_search_results(frame_id, search_query, search_results)
            
            processed_frames.append({
                "frame_id": frame_id,
                "timestamp": frame.timestamp_seconds,
                "frame_path": frame_path,
                "content_tags": [],
                "search_results": [r.__dict__ for r in search_results]
            })
        
        # Step 5: Generate and publish wiki page
        print("Generating wiki page...")
        wiki_title = f"Video Analysis: {video_filename}"
        wiki_content = self.wiki_client.generate_page_content(video_filename, processed_frames)
        
        # Save wiki page record
        wiki_id = self.db_client.save_wiki_page(
            user_id=user_id,
            title=wiki_title,
            content=wiki_content,
            video_id=video_id,
            frame_ids=frame_ids,
            category=category
        )
        
        # Publish to Feishu Wiki (under the category node when batching)
        print("Publishing to Feishu Wiki...")
        wiki_page = self.wiki_client.create_page(
            space_id=space_id,
            title=wiki_title,
            content=wiki_content,
            parent_node_token=parent_node_token
        )
        
        # Update video status to completed
        self.db_client.update_video_status(video_id, "processed")
        
        print(f"Processing complete! Wiki page: {wiki_page.get('node', {}).get('title')}")
        
        return {
            "video_id": video_id,
            "wiki_id": wiki_id,
            "feishu_wiki_url": wiki_page.get('node', {}).get('url'),
            "frames_processed": len(frames),
            "status": "completed"
        }

    def process_directory(self, directory: str, user_id: str, space_id: str,
                          recursive: bool = True, category_rules: dict = None,
                          continue_on_error: bool = True) -> dict:
        """Batch-process every video in a directory and return a summary dict."""
        processor = BatchProcessor(self)
        result = processor.process_directory(
            directory=directory,
            user_id=user_id,
            space_id=space_id,
            recursive=recursive,
            category_rules=category_rules,
            continue_on_error=continue_on_error,
        )
        return {
            "batch_id": result.batch_id,
            "directory": result.directory,
            "total": result.total,
            "succeeded": result.succeeded,
            "failed": result.failed,
            "items": [item.__dict__ for item in result.items],
        }

if __name__ == "__main__":
    import argparse
    
    import json

    parser = argparse.ArgumentParser(description="Process video(s) and generate analysis documentation")
    parser.add_argument("video_path", help="Path to an input video file, or a directory when --batch is set")
    parser.add_argument("--user-id", required=True, help="User ID (UUID)")
    parser.add_argument("--space-id", required=True, help="Feishu Wiki space ID")
    parser.add_argument("--batch", action="store_true", help="Treat video_path as a directory and process all videos inside")
    parser.add_argument("--no-recursive", action="store_true", help="In batch mode, do not descend into subdirectories")
    parser.add_argument("--category-rules", help="JSON object mapping path keywords to category names")
    parser.add_argument("--stop-on-error", action="store_true", help="In batch mode, stop at the first failing video")
    
    args = parser.parse_args()
    
    analyzer = VideoAnalyzer()

    if args.batch:
        rules = json.loads(args.category_rules) if args.category_rules else None
        result = analyzer.process_directory(
            directory=args.video_path,
            user_id=args.user_id,
            space_id=args.space_id,
            recursive=not args.no_recursive,
            category_rules=rules,
            continue_on_error=not args.stop_on_error,
        )
        print("\nBatch result:")
        print(json.dumps(result, indent=2, default=str))
    else:
        result = analyzer.process_video(args.video_path, args.user_id, args.space_id)
        print("\nResult:", result)