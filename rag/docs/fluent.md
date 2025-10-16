# Fluent 2 Design System Retrieval Document
# RAG-Optimized Format for Design System Validation

## ENTRY_001
**SOURCE_URL:** https://fluent2.microsoft.design/layout  
**SECTION:** Layout Foundation  
**SYSTEM:** Fluent 2 Design System  
**TOPIC:** Global Spacing Ramp and 4px Base Grid System  
**RETRIEVAL_TAGS:** spacing, 4px, grid, tokens, padding, margin, layout, baseline, proximity

Fluent 2 uses a 4px base unit for all spacing with a global spacing ramp designed to help makers get the best use out of consistent spacing while staying flexible to meet each experience's needs. Spacing tokens include: sizeNone (0px), size20 (2px), size40 (4px), size60 (6px), size80 (8px), size100 (10px), size120 (12px), size160 (16px), size200 (20px), size240 (24px), size280 (28px), size320 (32px), size360 (36px), size400 (40px), size480 (48px), size520 (52px), size560 (56px). The ramp includes values 2, 6, and 10 to account for extra padding in Fluent icons and help align icons to the 4px grid. Touch targets must be minimum 44px × 44px on iOS/Web, 48px × 48px on Android.

## ENTRY_002
**SOURCE_URL:** https://fluent2.microsoft.design/components/web/react/core/button/usage  
**SECTION:** Button Component  
**SYSTEM:** Fluent 2 Design System  
**TOPIC:** Button Types and Accessibility Specifications  
**RETRIEVAL_TAGS:** buttons, primary, secondary, subtle, split-button, menu-button, compound-button, accessibility

Fluent 2 provides several button types: Button (standard single action), Split Button (primary action with menu of related actions), Menu Button (toggles menu display), Compound Button (includes main title and description), and Toggle Button (two-state on/off behavior). Button text must pass 4.5:1 contrast ratio and icons must pass 3:1 contrast against their background. Only use one primary button per layout for the most important action. Primary buttons should have prominent placement either on top or to the left of other actions. Focus states should be clearly visible with proper keyboard navigation support.

## ENTRY_003
**SOURCE_URL:** https://fluent2.microsoft.design/elevation  
**SECTION:** Elevation and Shadow System  
**SYSTEM:** Fluent 2 Design System  
**TOPIC:** Shadow Tokens and Depth Hierarchy  
**RETRIEVAL_TAGS:** elevation, shadow, depth, layering, shadow-tokens, z-axis, blur

Fluent 2 uses elevation to create visual cues and convey levels of importance through shadows and light. The shadow system uses equations to generate consistent shadows based on blur values: Shadow 2 (2px blur, cards without edge and pressed floating action buttons), Shadow 4 (4px blur, cards and grid items), Shadow 8 (8px blur, command bars and tooltips), with higher values for increased elevation. Shadows combine sharp directional shadows (key) to define edges and soft diffused shadows (ambient) to imply distance. Windows platform uses strokes instead of key shadows to outline objects.

## ENTRY_004
**SOURCE_URL:** https://fluent2.microsoft.design/components/web/react/core/card/usage  
**SECTION:** Card Component  
**SYSTEM:** Fluent 2 Design System  
**TOPIC:** Card Layout and Shadow Behavior  
**RETRIEVAL_TAGS:** cards, containers, shadow, padding, radius, states, hover, elevation

Cards are content containers that organize and group related information. Cards use elevation through shadow tokens to create visual hierarchy and respond to interaction states. Rest state uses base shadow, hover state increases shadow for lifted appearance, pressed state reduces shadow for pressed-down effect. Cards can contain headers, body content, and actions with consistent spacing using the global spacing ramp. Maintain clear content hierarchy within cards using typography scale and proper spacing tokens.

## ENTRY_005
**SOURCE_URL:** https://fluent2.microsoft.design/typography  
**SECTION:** Typography System  
**SYSTEM:** Fluent 2 Design System  
**TOPIC:** Font Stack and Type Ramp  
**RETRIEVAL_TAGS:** typography, segoe-ui, font-size, line-height, text-styles, hierarchy, type-ramp

Fluent 2 uses Segoe UI as primary typeface with system font fallbacks for native platform experience. Web type ramp includes: Caption 2 (10px/14px), Caption 1 (12px/16px), Body 1 (14px/20px), Subtitle 2 (16px/22px), Subtitle 1 (20px/26px), Title 3 (24px/32px), Title 2 (28px/36px), Title 1 (32px/40px), Large Title (40px/52px), Display (68px/92px). Font weights: Regular (400), Semibold (600), Bold (700). Windows uses Segoe UI Variable with optical size axis for improved legibility at small sizes and personality at large sizes. Use semantic text tokens rather than hardcoded sizes.

## ENTRY_006
**SOURCE_URL:** https://fluent2.microsoft.design/color  
**SECTION:** Color System and Palettes  
**SYSTEM:** Fluent 2 Design System  
**TOPIC:** Neutral, Shared, Brand, and Semantic Colors  
**RETRIEVAL_TAGS:** color, tokens, brand, neutral, semantic, shared, contrast, accessibility, palettes

Fluent 2 defines three color palettes: Neutral (black, white, grays for surfaces, text, layout), Shared (aligned across M365 apps for avatars, calendars, badges), and Brand (product-specific colors for recognition). Semantic colors communicate feedback and status: red for danger, yellow for caution, green for positive feedback. Colors automatically adapt to light/dark themes. Interaction states generally darken components as users interact (rest → hover → selected), except Windows which lightens. Contrast requirements: 4.5:1 for normal text, 3:1 for large text and UI components. Use color tokens rather than hardcoded hex values.

## ENTRY_007
**SOURCE_URL:** https://fluent2.microsoft.design/layout  
**SECTION:** Grid System and Responsive Design  
**SYSTEM:** Fluent 2 Design System  
**TOPIC:** 12-Column Grid and Breakpoints  
**RETRIEVAL_TAGS:** grid, responsive, breakpoints, columns, gutters, margins, layout

Fluent 2 uses flexible grid systems with 12-column framework for its flexibility and easy division. Grid anatomy includes columns (building blocks), gutters (negative space between columns), margins (space outside grid), and regions (groupings forming composition elements). Breakpoints: small (< 479px), medium (< 639px), large (< 1023px), x-large (> 1024px), xx-large (> 1366px), xxx-large (> 1920px). Grid types include baseline grid (horizontal rows for text alignment), column grid (vertical fields), manuscript grid (single column blocks), and modular grid (vertical columns + horizontal rows creating matrix).

## ENTRY_008
**SOURCE_URL:** https://fluent2.microsoft.design/design-principles  
**SECTION:** Design Principles  
**SYSTEM:** Fluent 2 Design System  
**TOPIC:** Core Values and Philosophy  
**RETRIEVAL_TAGS:** principles, natural, focus, inclusive, microsoft, platform-aware, accessibility

Fluent 2 is guided by four core principles: 1) Natural on every platform - experiences adapt to device and platform, reusing native components 80% of time; 2) Built for focus - technology communicates and performs without getting in the way, reducing visual clutter; 3) One for all, all for one - includes diverse perspectives and abilities for better solutions; 4) Unmistakably Microsoft - signature experiences connect products with distinctive Microsoft feel through color, sound, illustration, and icons for brand recognition.

## ENTRY_009
**SOURCE_URL:** https://fluent2.microsoft.design/accessibility  
**SECTION:** Accessibility Guidelines  
**SYSTEM:** Fluent 2 Design System  
**TOPIC:** Inclusive Design and WCAG Standards  
**RETRIEVAL_TAGS:** accessibility, wcag, keyboard, screen-reader, contrast, inclusive, focus-management

Fluent 2 components meet or surpass WCAG 2.1 AA standards. Key requirements: logical heading hierarchies for scannable structure, keyboard navigation with visible focus indicators, color contrast ratios (4.5:1 for normal text, 3:1 for large text and UI components), responsive layouts that reflow content without horizontal scrolling up to 400% zoom, descriptive alt text for visual media, semantic HTML with proper ARIA labels. Focus should follow Z-pattern (left-right, top-bottom) and not be lost after closing temporary UI like dialogs.

## ENTRY_010
**SOURCE_URL:** https://fluent2.microsoft.design/iconography  
**SECTION:** Iconography System  
**SYSTEM:** Fluent 2 Design System  
**TOPIC:** Icon Collections and Specifications  
**RETRIEVAL_TAGS:** icons, system-icons, product-icons, themes, regular, filled, sizing, mit-license

Fluent iconography includes three collections: System icons (UI elements like command bars, navigation, status - open source MIT license), Product launch icons (represent Microsoft apps for identification and actions), File icons (document types). System icons support Regular (wayfinding, actions) and Filled (selected states, more visual weight) themes. Icon sizes vary by use case: 12px for information (too small for interaction), larger icons for smaller screens with bigger touch targets. Icons should be recognizable, functional, and easily understood with semantic purpose within layouts.

## ENTRY_011
**SOURCE_URL:** https://fluent2.microsoft.design/design-tokens  
**SECTION:** Design Token System  
**SYSTEM:** Fluent 2 Design System  
**TOPIC:** Global and Alias Token Architecture  
**RETRIEVAL_TAGS:** tokens, global, alias, semantic, theming, variables, consistency

Fluent 2 uses two-layer token system: Global tokens (context-agnostic raw values like hex codes, typography, border radius, stroke width, animation) and Alias tokens (semantic meaning for easy recognition and application). Alias tokens condense complex elements like shadows and typography into digestible formats. Token naming makes function immediately recognizable for consistent style application. Design tokens support OS theming for light, dark, high-contrast, and branded elements while ensuring sufficient color contrast across the system. Use tokens instead of hardcoded values for maintainability and consistency.

## ENTRY_012
**SOURCE_URL:** https://fluent2.microsoft.design/get-started/design  
**SECTION:** Figma UI Kits  
**SYSTEM:** Fluent 2 Design System  
**TOPIC:** Design Tool Integration and Asset Organization  
**RETRIEVAL_TAGS:** figma, ui-kits, components, design-to-development, variables, libraries

Fluent 2 UI kits in Figma provide design assets that map to code libraries for seamless design-to-development handoff. Four-tier organization: 1) Fluent 2 design language (source of truth for styling decisions), 2) Fluent 2 Core UI Kits (code-aligned building blocks for web, iOS, Android), 3) Copilot UI Kits (AI-focused components), 4) Labs UI Kits (experimental partner-led kits). Components organized in Assets panel with variants and properties mapping to code. Figma Variables enable light/dark mode toggling and support styling assets for Fluent and Copilot experiences.

## ENTRY_013
**SOURCE_URL:** https://fluent2.microsoft.design/content-design  
**SECTION:** Content Design Guidelines  
**SYSTEM:** Fluent 2 Design System  
**TOPIC:** Writing Standards and Content Accessibility  
**RETRIEVAL_TAGS:** content, writing, voice, tone, accessibility, punctuation, global-ready

Fluent 2 content design eases complex tasks by highlighting key decisions and simplifying interactions. Use second person (you, your) for friendly, human tone and avoid passive voice. Punctuation guidelines: use periods only after full sentences, always use question marks, avoid exclamation points except for celebratory situations. For accessibility: write short descriptive link text, avoid directional terms (above, below, left, right), create alt text for illustrative elements, organize content logically with headings and lists. Keep content global-ready and screen reader accessible.

## ENTRY_014
**SOURCE_URL:** https://fluent2.microsoft.design/material  
**SECTION:** Material and Surface Design  
**SYSTEM:** Fluent 2 Design System  
**TOPIC:** Surface Behaviors and Material Properties  
**RETRIEVAL_TAGS:** material, surface, mica, acrylic, transparency, backdrop, layering

Fluent 2 material system creates depth and layering through surface treatments. Materials include Mica (translucent surface that picks up desktop wallpaper), Acrylic (translucent material revealing content behind), and various backdrop effects. Materials help establish hierarchy and provide context for different interface layers. Surface elevation and material choices should reinforce content importance and user focus. Materials automatically adapt to light and dark themes while maintaining visual hierarchy and accessibility standards.

## ENTRY_015
**SOURCE_URL:** https://fluent2.microsoft.design/color-tokens  
**SECTION:** Web Alias Color Tokens  
**SYSTEM:** Fluent 2 Design System  
**TOPIC:** Color Token Categories and Usage  
**RETRIEVAL_TAGS:** color-tokens, neutral, brand, status, alias, theming, systematic-color

Fluent 2 color tokens organized into alias groups: Neutral Background (colorNeutralBackground1 through colorNeutralBackground6 for surfaces with states), Brand colors (product-specific identity), Status colors (semantic feedback), and Generic tokens (broader use cases). Each token includes rest, hover, pressed, and selected states. Neutral tokens provide base for surfaces and text, brand tokens reinforce identity, status tokens communicate meaning (success, error, warning), generic tokens support flexible use cases. Working with aliases instead of raw values ensures systematic application, theme flexibility, and reliable scaling across products.