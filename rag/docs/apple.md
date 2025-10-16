# Apple Human Interface Guidelines Retrieval Document
# RAG-Optimized Format for Design System Validation

## ENTRY_001
SOURCE_URL: https://developer.apple.com/design/human-interface-guidelines/layout
SECTION: Layout and Organization
SYSTEM: Apple HIG
TOPIC: Layout Principles and Safe Areas
RETRIEVAL_TAGS: layout, safe-area, margins, spacing, adaptive, responsive

iOS uses adaptive layouts that respond to different screen sizes, orientations, and device capabilities. Respect safe area insets to avoid content being obscured by device features like notches or home indicators. Standard margins are 16pt on iPhone, 20pt on iPad. Use multiples of 8pt for consistent spacing: 8pt, 16pt, 24pt, 32pt. Maintain minimum 44pt × 44pt touch targets for all interactive elements. Content should flow naturally and remain accessible across all supported device sizes.

## ENTRY_002
SOURCE_URL: https://developer.apple.com/design/human-interface-guidelines/buttons
SECTION: Button Design and Usage
SYSTEM: Apple HIG
TOPIC: Button Types and Specifications
RETRIEVAL_TAGS: buttons, filled, tinted, gray, plain, system, touch-target, states

iOS provides four main button styles: Filled (solid background for primary actions), Tinted (transparent background with colored text for secondary actions), Gray (gray background for cancel/dismiss actions), and Plain (text-only for tertiary actions). All buttons must have minimum 44pt height and width for accessibility. Button states include Normal, Highlighted (reduced opacity 30-50%), Disabled (40% opacity), and Focused (for keyboard navigation). Use SF Symbols at 20pt or 22pt scale when adding icons to buttons.

## ENTRY_003
SOURCE_URL: https://developer.apple.com/design/human-interface-guidelines/typography
SECTION: Typography and Dynamic Type
SYSTEM: Apple HIG
TOPIC: Text Styles and Scaling
RETRIEVAL_TAGS: typography, dynamic-type, text-styles, san-francisco, accessibility, scaling

Apple platforms use San Francisco font family. Support Dynamic Type to accommodate user's preferred reading size. Text styles include: Large Title (34pt), Title 1 (28pt), Title 2 (22pt), Title 3 (20pt), Headline (17pt Semibold), Body (17pt Regular - default for most content), Callout (16pt), Subheadline (15pt), Footnote (13pt), Caption 1 (12pt), Caption 2 (11pt). Line height is typically 1.2-1.4× font size. Test layouts with largest Dynamic Type sizes to ensure content remains readable and interface remains functional.

## ENTRY_004
SOURCE_URL: https://developer.apple.com/design/human-interface-guidelines/color
SECTION: Color and Visual Design
SYSTEM: Apple HIG
TOPIC: System Colors and Accessibility
RETRIEVAL_TAGS: color, system-colors, light-mode, dark-mode, contrast, accessibility, semantic

Use system colors that automatically adapt to light and dark modes: System Blue (#007AFF light, #0A84FF dark), System Red (#FF3B30 light, #FF453A dark), System Green (#34C759 light, #32D74B dark). For text, use semantic colors: Label (primary text), Secondary Label (60% opacity), Tertiary Label (30% opacity), Quaternary Label (18% opacity for disabled text). Background colors include System Background, Secondary System Background, and Tertiary System Background. Always test in both appearance modes and ensure minimum 4.5:1 contrast ratio for text.

## ENTRY_005
SOURCE_URL: https://developer.apple.com/design/human-interface-guidelines/navigation-bars
SECTION: Navigation Components
SYSTEM: Apple HIG
TOPIC: Navigation Bar Specifications
RETRIEVAL_TAGS: navigation, nav-bar, title, back-button, height, large-title

Navigation bars have height of 44pt in compact layouts, 96pt with large title. Large titles automatically collapse to standard size when scrolling. Navigation bar items should use standard system icons and maintain consistent placement. Back button appears automatically and includes page title when space permits. Navigation bar supports translucent background that blurs content behind it. Always provide clear visual hierarchy and avoid overcrowding with too many navigation items.

## ENTRY_006
SOURCE_URL: https://developer.apple.com/design/human-interface-guidelines/tab-bars
SECTION: Tab Navigation
SYSTEM: Apple HIG
TOPIC: Tab Bar Design and Layout
RETRIEVAL_TAGS: tab-bar, tabs, navigation, icons, sf-symbols, height

Tab bars have height of 49pt on standard displays, 83pt when accounting for safe area on newer devices. Support 3-5 tabs maximum for optimal usability. Use SF Symbols at 25pt scale for tab icons. Selected tab should have clear visual distinction through color and icon style changes. Tab labels should be concise, typically 1-2 words. Avoid using tab bars for temporary states or actions - use toolbars instead. Tab bar icons should represent their sections clearly without requiring labels.

## ENTRY_007
SOURCE_URL: https://developer.apple.com/design/human-interface-guidelines/lists-and-tables
SECTION: List and Table Design
SYSTEM: Apple HIG
TOPIC: Table View Specifications
RETRIEVAL_TAGS: table-view, lists, rows, cells, height, separators, disclosure

Table view rows have minimum height of 44pt for standard cells. Cell padding is 16pt horizontal, 12pt vertical. Use disclosure indicators (›) for navigable items, checkmarks for selections, and detail buttons (i) for additional information. Table sections can have headers and footers with appropriate text styling. Separator lines should inset 16pt from leading edge to align with cell content. Support swipe actions for common operations like delete or archive. Provide clear visual feedback for selections and interactions.

## ENTRY_008
SOURCE_URL: https://developer.apple.com/design/human-interface-guidelines/modality
SECTION: Modal Presentations
SYSTEM: Apple HIG
TOPIC: Sheets, Popovers, and Alerts
RETRIEVAL_TAGS: modal, sheet, popover, alert, presentation, dismiss

Prefer sheets over full-screen modals when possible. Sheets have 10pt corner radius and can be dismissed by dragging down or tapping outside. Provide clear dismiss affordances like "Cancel" or "Done" buttons. Popovers should point to their originating element and automatically adjust position to remain on screen. Alerts should be used sparingly for critical information requiring immediate user attention. Modal content should be focused and allow users to complete their task efficiently without losing context.

## ENTRY_009
SOURCE_URL: https://developer.apple.com/design/human-interface-guidelines/accessibility
SECTION: Accessibility Requirements
SYSTEM: Apple HIG
TOPIC: VoiceOver and Assistive Technologies
RETRIEVAL_TAGS: accessibility, voiceover, labels, hints, touch-targets, contrast, dynamic-type

All interactive elements must have meaningful accessibility labels for VoiceOver users. Provide accessibility hints for complex interactions. Ensure minimum 44pt × 44pt touch targets with adequate spacing between targets (minimum 8pt). Support Dynamic Type scaling and test layouts at largest sizes. Use sufficient color contrast and never rely solely on color to convey information. Provide alternative text for images and ensure all app functionality is available through assistive technologies. Test thoroughly with VoiceOver enabled.

## ENTRY_010
SOURCE_URL: https://developer.apple.com/design/human-interface-guidelines/sf-symbols
SECTION: SF Symbols Usage
SYSTEM: Apple HIG
TOPIC: Icon System and Guidelines
RETRIEVAL_TAGS: sf-symbols, icons, symbols, sizing, alignment, variants, accessibility

SF Symbols provides consistent icon system with multiple weights and scales. Standard sizes: 13pt (small), 17pt (medium), 20pt (large), 22pt (extra large). Symbols automatically align with text baselines and support Dynamic Type scaling. Use appropriate symbol variants (fill, slash, badge) to convey different states. Ensure symbols remain recognizable at all sizes and provide alternative text labels for accessibility. Don't modify SF Symbols - use them as provided to maintain visual consistency across the system.
