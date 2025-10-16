# Material Design Retrieval Document
# RAG-Optimized Format for Design System Validation

## ENTRY_001
SOURCE_URL: https://m3.material.io/foundations/layout/understanding-layout/overview
SECTION: Layout Fundamentals
SYSTEM: Material Design 3
TOPIC: Grid System
RETRIEVAL_TAGS: layout, grid, spacing, columns, responsive

Material Design uses a 12-column grid system for desktop, 8-column for tablet, and 4-column for mobile. Grid provides consistent structure and alignment across different screen sizes. Column width is fluid and adapts to viewport, but gutters remain fixed at 16dp (mobile) or 24dp (tablet/desktop). Margins are 16dp on mobile, 24dp on tablet, and range from 24-40dp on desktop depending on content width.

## ENTRY_002
SOURCE_URL: https://m3.material.io/foundations/layout/applying-layout/spacing
SECTION: Spacing System
SYSTEM: Material Design 3
TOPIC: 8dp Grid System
RETRIEVAL_TAGS: spacing, 8dp, baseline, grid, padding, margin, measurements

All spacing in Material Design follows an 8dp baseline grid system. This means all margins, padding, and spacing between elements should be multiples of 8dp: 8, 16, 24, 32, 40, 48, 56, 64dp etc. This creates visual rhythm and consistency. Touch targets must be minimum 48dp × 48dp for accessibility. Small components can use 4dp increments but should align to 8dp boundaries when grouped.

## ENTRY_003
SOURCE_URL: https://m3.material.io/styles/elevation/tokens
SECTION: Elevation Tokens
SYSTEM: Material Design 3
TOPIC: Shadow and Elevation System
RETRIEVAL_TAGS: elevation, shadow, depth, surface, z-index, layers

Material Design defines 6 elevation levels: Level 0 (0dp - no shadow), Level 1 (1dp - cards at rest), Level 2 (2dp - raised buttons), Level 3 (3dp - refresh indicators), Level 4 (4dp - app bars), Level 5 (6dp - snackbars), Level 6 (8dp - menus). Each level has specific shadow values combining key shadow (directional) and ambient shadow (soft). Never create custom shadows - always use predefined elevation tokens.

## ENTRY_004
SOURCE_URL: https://m3.material.io/components/buttons/overview
SECTION: Button Types and Usage
SYSTEM: Material Design 3
TOPIC: Button Component Specifications
RETRIEVAL_TAGS: buttons, filled, outlined, text, elevated, tonal, primary, secondary

Material Design provides 5 button types: Filled (highest emphasis, solid background), Outlined (medium emphasis, transparent with border), Text (low emphasis, no background/border), Elevated (high emphasis with shadow), and Tonal (medium emphasis with tinted background). Filled buttons use primary color for main actions like "Save" or "Submit". Outlined buttons are for secondary actions like "Cancel". Text buttons are for low-priority actions in dialogs or toolbars.

## ENTRY_005
SOURCE_URL: https://m3.material.io/components/buttons/specs
SECTION: Button Specifications
SYSTEM: Material Design 3
TOPIC: Button Dimensions and States
RETRIEVAL_TAGS: button, height, padding, radius, states, hover, focus, pressed, disabled

Standard button height is 40dp with 24dp horizontal padding for text buttons and 16dp for icon buttons. Corner radius is 20dp for fully rounded buttons, or 4-12dp for less rounded variants. Button states include: Enabled (default), Hovered (8% surface overlay), Focused (12% overlay + focus ring), Pressed (12% overlay), and Disabled (38% opacity, non-interactive). Icon size within buttons is 18dp when paired with text.

## ENTRY_006
SOURCE_URL: https://m3.material.io/components/cards/overview
SECTION: Card Component Design
SYSTEM: Material Design 3
TOPIC: Card Layout and Types
RETRIEVAL_TAGS: cards, container, content, surface, elevation, outline

Cards are surfaces containing content and actions on a single subject. Three card types: Elevated (uses shadow for depth), Filled (uses fill color), and Outlined (uses stroke). Minimum width is 280dp on mobile, 344dp on desktop. Corner radius is 12dp. Internal padding is 16dp on mobile, 24dp on desktop. Cards can contain headers, media, supporting text, and action areas with consistent 8dp spacing between elements.

## ENTRY_007
SOURCE_URL: https://m3.material.io/foundations/overview/principles
SECTION: Accessibility Requirements
SYSTEM: Material Design 3
TOPIC: Color Contrast and Touch Targets
RETRIEVAL_TAGS: accessibility, contrast, WCAG, color-blind, touch-target, screen-reader

All text must meet WCAG 2.1 contrast requirements: 4.5:1 for normal text, 3:1 for large text (18pt+), 3:1 for UI components. Never rely solely on color to convey information - use text labels, icons, or patterns. All interactive elements must have minimum 48dp × 48dp touch targets. Provide meaningful content descriptions for screen readers. Support dynamic text scaling and high contrast modes.

## ENTRY_008
SOURCE_URL: https://m3.material.io/styles/typography/type-scale
SECTION: Typography Scale
SYSTEM: Material Design 3
TOPIC: Text Styles and Hierarchy
RETRIEVAL_TAGS: typography, font-size, line-height, font-weight, roboto, scale

Material Design uses 15 predefined text styles: Display Large (57sp), Display Medium (45sp), Display Small (36sp), Headline Large (32sp), Headline Medium (28sp), Headline Small (24sp), Title Large (22sp, Medium weight), Title Medium (16sp, Medium), Title Small (14sp, Medium), Body Large (16sp), Body Medium (14sp), Body Small (12sp), Label Large (14sp, Medium), Label Medium (12sp, Medium), Label Small (11sp, Medium). Default font is Roboto. Line height is typically 1.5× font size for readability.

## ENTRY_009
SOURCE_URL: https://m3.material.io/styles/color/roles
SECTION: Color System and Roles
SYSTEM: Material Design 3
TOPIC: Color Tokens and Usage
RETRIEVAL_TAGS: color, primary, secondary, tertiary, error, surface, on-color, tonal-palette

Material Design uses systematic color roles: Primary (main brand color for key components), Secondary (accent color for less prominent elements), Tertiary (contrasting accent for highlights), Error (for error states), and Surface (component backgrounds). Each color has corresponding "on-color" variants for text/icons. Colors are generated from tonal palettes with multiple shades. Always use semantic color tokens rather than hardcoded hex values to ensure proper theming and accessibility.

## ENTRY_010
SOURCE_URL: https://m3.material.io/components/buttons/guidelines
SECTION: Button Usage Guidelines
SYSTEM: Material Design 3
TOPIC: Button Placement and Best Practices
RETRIEVAL_TAGS: button, usage, placement, actions, hierarchy, confirmation

Use only one filled button per view to maintain clear action hierarchy. Place primary action button on the right in LTR layouts, left in RTL layouts. In dialogs, confirming action goes on the right, dismissive on the left. Avoid using buttons for navigation - use links or tabs instead. Group related buttons with consistent spacing. For destructive actions, use error/danger styling. Button text should be concise action words like "Save", "Delete", "Continue".
