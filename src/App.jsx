import { useState } from 'react'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-16">
        <div className="max-w-4xl mx-auto">
          <header className="text-center mb-12">
            <h1 className="text-5xl font-bold text-gray-900 mb-4">
              Issac Bane Chase
            </h1>
            <p className="text-xl text-gray-600">
              Welcome to your new web application
            </p>
          </header>

          <div className="bg-white rounded-lg shadow-xl p-8 mb-8">
            <div className="text-center">
              <h2 className="text-3xl font-semibold text-gray-800 mb-6">
                Getting Started
              </h2>
              <p className="text-gray-600 mb-8">
                This is a React application built with Vite and Tailwind CSS
              </p>
              
              <div className="flex justify-center items-center space-x-4 mb-8">
                <button
                  onClick={() => setCount((count) => count + 1)}
                  className="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 px-6 rounded-lg transition duration-200 shadow-md hover:shadow-lg"
                >
                  Count is {count}
                </button>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="p-6 bg-blue-50 rounded-lg">
                  <h3 className="text-lg font-semibold text-blue-900 mb-2">React</h3>
                  <p className="text-blue-700 text-sm">
                    A JavaScript library for building user interfaces
                  </p>
                </div>
                <div className="p-6 bg-purple-50 rounded-lg">
                  <h3 className="text-lg font-semibold text-purple-900 mb-2">Vite</h3>
                  <p className="text-purple-700 text-sm">
                    Next generation frontend tooling
                  </p>
                </div>
                <div className="p-6 bg-indigo-50 rounded-lg">
                  <h3 className="text-lg font-semibold text-indigo-900 mb-2">Tailwind CSS</h3>
                  <p className="text-indigo-700 text-sm">
                    A utility-first CSS framework
                  </p>
                </div>
              </div>
            </div>
          </div>

          <footer className="text-center text-gray-600">
            <p>Edit <code className="bg-gray-200 px-2 py-1 rounded">src/App.jsx</code> to get started</p>
          </footer>
        </div>
      </div>
    </div>
  )
}

export default App
