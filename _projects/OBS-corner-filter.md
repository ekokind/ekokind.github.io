---
title: OBS Corner Filter Documentation
image: theme/img/project-photos/glow.png
image_alt: "Example of OBS filter used on white background"
---

# OBS Rounded Corner with Shadow and Glow Filter: Complete Guide & Tutorial

A professional-looking rounded corner effect for  OBS Studio streams and recordings. Perfect for webcam overlays, screen captures, and video sources. 

<img src="{{ page.image | relative_url }}" 
     alt="{{ page.image_alt }}" 
     style="max-width:500px; height:auto; display:block; margin: 1em auto;">

### [📥 Link to Download Here](/theme/OBS-stuff/rounded_camera.effect)

## 🎯 Overview

The **OBS Rounded Corners Shader Filter** is a custom HLSL shader that adds professional rounded corners, drop shadows, borders, and glow effects to any video source in OBS Studio. This filter is perfect for:

- **Webcam overlays** with modern rounded aesthetics
- **Screen capture** with polished presentation
- **Gaming streams** with clean video layouts
- **Professional broadcasts** and presentations
- **Social media content** creation

### ✨ Key Features

```
✅ Customizable drop shadows with blur and opacity controls
✅ Optional borders with color customization
✅ Glow effects for enhanced visual appeal
✅ Standardized parameter system (0.1 - 5.0 scale)
✅ Real-time preview and adjustment
```

## 📋 Requirements

### OBS Studio Version
- **OBS Studio 27.0+** (recommended)
- **OBS Studio 26.x** (compatible)

### Required Plugin
- **OBS ShaderFilter Plugin** by Exeldro
- Download: [GitHub Release Page](https://github.com/exeldro/obs-shaderfilter/releases)

### System Requirements
- **Windows 10/11** with DirectX 11 support
- **macOS 10.15+** (compatibility may vary)
- **Linux** with OpenGL 3.3+ support

## 🚀 Installation

### Step 1: Install OBS ShaderFilter Plugin

1. Download the latest ShaderFilter plugin from the [official GitHub repository](https://github.com/exeldro/obs-shaderfilter/releases)
2. Extract the downloaded file
3. Copy the plugin files to your OBS plugins directory:

```bash
# Windows
C:\Program Files\obs-studio\obs-plugins\64bit\

# macOS
/Applications/OBS.app/Contents/PlugIns/

# Linux
/usr/lib/obs-plugins/
# or
~/.config/obs-studio/plugins/
```

4. Restart OBS Studio

### Step 2: Download the Shader File

1. Download `rounded_corners_glow.effect` [Download here!](/theme/OBS-stuff/rounded_camera.effect)
2. Save the file in an easily accessible location

```
📁 Recommended Locations:
   📄 ~\Documents\OBS\Shaders\rounded_corners_glow.effect
   📄 ~\Desktop\rounded_corners_glow.effect
   📄 C:\OBS-Shaders\rounded_corners_glow.effect
```

### Step 3: Apply the Filter

```
1. Right-click your video source in OBS
2. Select "Filters" from the context menu
3. Click the "+" button under "Effect Filters" and choose "User-defined Shader"
4. Check the "Load shader text from file" button
5. Browse and select your shader file
6. Check the box for "Use Effect File (.effect)"
7. Click "OK" to apply and close the window
```

## ⚙️ Configuration

### Basic Setup

Once applied, the filter will add rounded corners to your video source. The default settings provide a balanced, professional look suitable for most use cases.

### 📂 Filter Order

For optimal results, apply filters in this order:

```
1. Color Correction (if needed)
   ↓
2. Crop/Pad (if needed)
   ↓
3. Rounded Corners Shader ← This filter
   ↓
4. Scaling/Transform (if needed)
```

## 🎛️ Parameter Guide

All parameters use a **standardized 0.1 to 5.0 scale** for intuitive adjustment:

### 🔘 Corner Roundness

```yaml
Range: 0.1 - 5.0
Default: 1.0
Description: Controls how rounded the corners appear

Examples:
  0.1 → Subtle corner rounding
  1.0 → Moderate roundness (recommended)
  5.0 → Very round, almost circular or oval
```

### 🌑 Shadow Controls

#### Shadow Offset X & Y

```yaml
Range: 0.1 - 5.0 (each axis)
Default: 1.0
Description: Controls shadow position

Examples:
  0.1 → Minimal shadow distance
  1.0 → Moderate shadow offset
  5.0 → Far shadow distance
```

#### Shadow Blur

```yaml
Range: 0.1 - 5.0
Default: 2.0
Description: Controls shadow softness

Examples:
  0.1 → Sharp, crisp shadow edges
  2.0 → Smooth, natural shadow
  5.0 → Very soft, diffused shadow
```

#### Shadow Opacity

```yaml
Range: 0.1 - 5.0
Default: 3.0
Description: Controls shadow visibility

Examples:
  0.1 → Very faint shadow
  3.0 → Medium shadow strength
  5.0 → Solid, dark shadow
```

### 🔲 Border Settings

#### Border Width

```yaml
Range: 0.1 - 5.0
Default: 0.5
Description: Controls border thickness

Examples:
  0.1 → Thin border line
  0.5 → Moderate border
  5.0 → Thick border
```

#### Border Color

```yaml
Type: RGBA Color Picker
Default: White (1.0, 1.0, 1.0, 0.8)
Description: Customize border color and transparency

Common Colors:
  White:  rgba(255, 255, 255, 0.8)
  Black:  rgba(0, 0, 0, 0.8)
  Blue:   rgba(0, 123, 255, 0.8)
  Brand:  rgba(your, brand, colors, 0.8)
```

### ✨ Glow Effect

#### Enable Glow

```yaml
Type: Boolean (True/False)
Default: False
Description: Toggle glow effect on/off
```

#### Glow Intensity

```yaml
Range: 0.1 - 5.0
Default: 2.0
Description: Controls glow brightness

Examples:
  0.1 → Subtle glow effect
  2.0 → Moderate glow
  5.0 → Bright, prominent glow
```

## 🔧 Troubleshooting

### Common Issues and Solutions

#### ❌ "Unknown Error" When Loading Shader

**Solutions (try in order):**

```
1. Change file extension:
   .shader → .effect
   
2. Verify plugin installation:
   - Check if "Shader Filter" appears in filter menu
   - Reinstall ShaderFilter plugin if missing
   
3. Check OBS version:
   - Requires OBS 26.0 or newer
   - Update OBS if outdated
   
4. Try simplified shader:
   - Use basic version for older systems
```

#### ❌ Filter Not Appearing in Menu

**Problem:** ShaderFilter plugin not installed correctly

**Solution:**
```bash
# Reinstall steps:
1. Download correct version for your OS
2. Extract to proper plugin directory
3. Restart OBS Studio
4. Verify installation in Filters menu
```


#### ❌ Rounded Corners Not Matching Crop

**Problem:** Filter applied before cropping

**Solution:**
```
Filter Order Fix:
1. Remove Rounded Corners filter
2. Apply Crop/Pad filter first
3. Re-add Rounded Corners filter
4. Shader auto-detects new dimensions
```




### 🎨 Creative Presets

#### Professional Presentations
```yaml
Settings:
  Corner Roundness: 1.0
  Shadow Offset X: 0.8
  Shadow Offset Y: 0.8
  Shadow Blur: 1.5
  Shadow Opacity: 2.0
  Border Width: 0.3
  Border Color: White or Brand Color
```

#### Gaming Streams
```yaml
Settings:
  Corner Roundness: 2.0
  Shadow Offset X: 1.5
  Shadow Offset Y: 1.5
  Shadow Blur: 3.0
  Shadow Opacity: 4.0
  Enable Glow: True
  Glow Intensity: 2.5
```

#### Social Media Content
```yaml
Settings:
  Corner Roundness: 2.5
  Shadow Offset X: 2.0
  Shadow Offset Y: 2.0
  Shadow Blur: 4.0
  Shadow Opacity: 3.5
  Border Width: 1.0
  Bright Colors: Custom RGBA
```

## ❓ FAQ

### Q: Does this work with all video sources?
```
A: Yes, compatible with:
   ✅ Webcams
   ✅ Screen captures  
   ✅ Video files
   ✅ Browser sources
   ✅ Game captures
   ✅ Any OBS video source
```

### Q: Can I use this with multiple sources simultaneously?
```
A: Yes, but best practices:
   ✅ Apply to individual sources
   ❌ Avoid applying to entire scene
   ⚡ Better performance per-source
```

### Q: What's the difference between .shader and .effect files?
```
.effect files:
  ✅ Better OBS compatibility
  ✅ Enhanced parameter controls
  ✅ More stable loading
  
.shader files:
  ⚠️ May work depending on system
  ⚠️ Less reliable parameter UI
  
Recommendation: Try .effect first
```


### Q: Can I animate the parameters?
```
Current Limitations:
  ❌ No built-in animation support
  ❌ Static parameters only

### Q: Is this compatible with other OBS plugins?
```yaml
Compatibility:
  ✅ Most OBS plugins work fine
  ⚠️ Filter order matters
  
Best Practice Order:
  1. Color Correction
  2. Crop/Pad
  3. Rounded Corners ← This filter
  4. Other effects
```

### Q: Can I save different presets?
```yaml
Preset Management:
  Scene Collections:
    - Save entire configurations
    - Include all filter settings
    - Quick switching between setups
    
  Manual Backup:
    - Note down parameter values
    - Screenshot configurations
    - Document preferred settings
```

---

## 🔗 Support and Resources

### 📚 Documentation Links
- **OBS Forum**: [OBS Project Community](https://obsproject.com/forum/)
- **ShaderFilter Plugin**: [GitHub Issues](https://github.com/exeldro/obs-shaderfilter/issues)
- **OBS Discord**: Official OBS Discord server for real-time help

### 🏷️ Related Keywords
```
Primary: OBS Studio filters, OBS webcam overlay, OBS rounded corners
Secondary: streaming effects, broadcast graphics, OBS shader tutorial
Technical: webcam effects, screen capture effects, OBS plugins
Content: streaming setup, content creation tools, video filters
Broadcasting: live streaming graphics, OBS custom effects
```

### 📥 Quick Download Links
```yaml
Required Downloads:
  OBS Studio: https://obsproject.com/download
  ShaderFilter: https://github.com/exeldro/obs-shaderfilter/releases
```