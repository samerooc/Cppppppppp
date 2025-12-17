# Video Player Application

## Overview
A feature-rich web-based video player with support for HLS and DASH streaming formats. The player includes controls for playback, seeking, volume, speed adjustment, quality selection, and fullscreen mode.

## Project Structure
- `index.html` - Single-page video player application with embedded CSS and JavaScript
- `server.py` - Simple Python HTTP server to serve the static files

## How to Use
The video player expects a video URL to be passed via query string parameter. Access the player with:
```
?url=<video_url>
```

## Features
- HLS and DASH streaming support via hls.js and Shaka Player
- Playback controls (play/pause, seek, skip)
- Volume control
- Speed adjustment (0.5x to 2x)
- Quality selection for adaptive streams
- Jump to specific time
- Fullscreen mode
- Double-tap to skip (mobile-friendly)
- Auto-hide controls

## Technical Details
- Frontend: Static HTML/CSS/JavaScript
- Server: Python's built-in HTTP server on port 5000
- External dependencies loaded via CDN:
  - Font Awesome for icons
  - hls.js for HLS streaming
  - Shaka Player for DASH streaming
