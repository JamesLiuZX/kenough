import './globals.css'
import Link from 'next/link';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <nav style={{ backgroundColor: '#ADD8E6', padding: '10px' }}>
          <Link href="/">
            <span style={{ color: 'white', fontSize: '24px', cursor: 'pointer' }}>Condensation</span>
          </Link>
        </nav>
        {children}
      </body>
    </html>
  )
}
