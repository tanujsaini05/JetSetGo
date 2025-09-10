import React, { useState } from 'react';
import { Plane, MapPin, DollarSign, Users, Calendar, Clock, Loader2 } from 'lucide-react';

interface TripRequest {
  from_city: string;
  destination: string;
  budget: number;
  people: number;
  stay: number;
  start_date: string;
}

interface TripResponse {
  travel_plan: string;
}

function App() {
  const [formData, setFormData] = useState<TripRequest>({
    from_city: '',
    destination: '',
    budget: 0,
    people: 1,
    stay: 1,
    start_date: '',
  });
  
  const [isLoading, setIsLoading] = useState(false);
  const [travelPlan, setTravelPlan] = useState<string>('');
  const [error, setError] = useState<string>('');

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, type } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'number' ? Number(value) : value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError('');
    setTravelPlan('');

    try {
      const response = await fetch('https://your-api-endpoint.com/plan-trip', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error('Failed to generate travel plan');
      }

      const data: TripResponse = await response.json();
      setTravelPlan(data.travel_plan);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setIsLoading(false);
    }
  };
  
  const formatToMarkdown = (content: string): string => {
    // The content from your API is already in markdown format, return as-is
    return content;
  };

  const isFormValid = () => {
    return formData.from_city && 
           formData.destination && 
           formData.budget > 0 && 
           formData.people > 0 && 
           formData.stay > 0 && 
           formData.start_date;
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="flex items-center justify-center mb-4">
            <Plane className="w-12 h-12 text-blue-600 mr-3" />
            <h1 className="text-4xl font-bold text-gray-800">AI Trip Planner</h1>
          </div>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Plan your perfect trip with AI-powered recommendations. Just fill in your details and let our intelligent system create a personalized travel itinerary for you.
          </p>
        </div>

        <div className="max-w-4xl mx-auto">
          <div className="grid lg:grid-cols-2 gap-8">
            {/* Form Section */}
            <div className="bg-white rounded-2xl shadow-xl p-8 h-fit">
              <h2 className="text-2xl font-semibold text-gray-800 mb-6 flex items-center">
                <MapPin className="w-6 h-6 mr-2 text-blue-600" />
                Trip Details
              </h2>
              
              <form onSubmit={handleSubmit} className="space-y-6">
                <div className="grid sm:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      From City
                    </label>
                    <input
                      type="text"
                      name="from_city"
                      value={formData.from_city}
                      onChange={handleInputChange}
                      required
                      className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 hover:border-gray-400"
                      placeholder="New York"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Destination
                    </label>
                    <input
                      type="text"
                      name="destination"
                      value={formData.destination}
                      onChange={handleInputChange}
                      required
                      className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 hover:border-gray-400"
                      placeholder="Paris"
                    />
                  </div>
                </div>

                <div className="grid sm:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2 flex items-center">
                      <DollarSign className="w-4 h-4 mr-1" />
                      Budget ($)
                    </label>
                    <input
                      type="number"
                      name="budget"
                      value={formData.budget || ''}
                      onChange={handleInputChange}
                      required
                      min="1"
                      className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 hover:border-gray-400"
                      placeholder="2000"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2 flex items-center">
                      <Users className="w-4 h-4 mr-1" />
                      Number of People
                    </label>
                    <input
                      type="number"
                      name="people"
                      value={formData.people}
                      onChange={handleInputChange}
                      required
                      min="1"
                      className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 hover:border-gray-400"
                      placeholder="2"
                    />
                  </div>
                </div>

                <div className="grid sm:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2 flex items-center">
                      <Clock className="w-4 h-4 mr-1" />
                      Stay Duration (days)
                    </label>
                    <input
                      type="number"
                      name="stay"
                      value={formData.stay}
                      onChange={handleInputChange}
                      required
                      min="1"
                      className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 hover:border-gray-400"
                      placeholder="7"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2 flex items-center">
                      <Calendar className="w-4 h-4 mr-1" />
                      Start Date
                    </label>
                    <input
                      type="date"
                      name="start_date"
                      value={formData.start_date}
                      onChange={handleInputChange}
                      required
                      className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 hover:border-gray-400"
                    />
                  </div>
                </div>

                <button
                  type="submit"
                  disabled={!isFormValid() || isLoading}
                  className="w-full bg-gradient-to-r from-blue-600 to-purple-600 text-white py-4 px-6 rounded-lg font-semibold text-lg transition-all duration-200 hover:from-blue-700 hover:to-purple-700 disabled:opacity-50 disabled:cursor-not-allowed transform hover:scale-[1.02] active:scale-[0.98] shadow-lg hover:shadow-xl flex items-center justify-center space-x-2"
                >
                  {isLoading ? (
                    <>
                      <Loader2 className="w-5 h-5 animate-spin" />
                      <span>Planning Your Trip...</span>
                    </>
                  ) : (
                    <>
                      <Plane className="w-5 h-5" />
                      <span>Plan My Trip</span>
                    </>
                  )}
                </button>
              </form>
            </div>

            {/* Results Section */}
            <div className="space-y-6">
              {/* Live API Notice */}
              <div className="bg-green-50 border border-green-200 rounded-2xl p-6">
                <div className="flex items-center space-x-3">
                  <div className="flex-shrink-0">
                    <div className="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center">
                      <span className="text-green-600 text-sm font-medium">✓</span>
                    </div>
                  </div>
                  <div>
                    <h3 className="text-green-800 font-medium">Live AI Backend</h3>
                    <p className="text-green-700 text-sm">Connected to real AI-powered trip planning service via ngrok.</p>
                  </div>
                </div>
              </div>
              
              {error && (
                <div className="bg-red-50 border border-red-200 rounded-2xl p-6">
                  <div className="flex items-center space-x-3">
                    <div className="flex-shrink-0">
                      <div className="w-8 h-8 bg-red-100 rounded-full flex items-center justify-center">
                        <span className="text-red-600 text-sm font-medium">!</span>
                      </div>
                    </div>
                    <div>
                      <h3 className="text-red-800 font-medium">Error</h3>
                      <p className="text-red-700 text-sm">{error}</p>
                    </div>
                  </div>
                </div>
              )}
              
              {travelPlan && (
                <div className="bg-white rounded-2xl shadow-xl p-8 animate-in slide-in-from-bottom-4 duration-500">
                  <div className="flex items-center space-x-3 mb-6">
                    <div className="w-10 h-10 bg-gradient-to-r from-green-400 to-blue-500 rounded-full flex items-center justify-center">
                      <Plane className="w-5 h-5 text-white" />
                    </div>
                    <h3 className="text-2xl font-semibold text-gray-800">Your Travel Plan</h3>
                  </div>
                  
                  <div className="prose prose-lg max-w-none">
                    <div className="bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl p-6 text-gray-700 leading-relaxed">
                      <div 
                        className="markdown-content"
                        dangerouslySetInnerHTML={{ 
                          __html: travelPlan
                            .replace(/\n/g, '<br>')
                            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                            .replace(/\*(.*?)\*/g, '<em>$1</em>')
                            .replace(/^# (.*$)/gm, '<h1 class="text-2xl font-bold mb-4 text-gray-800">$1</h1>')
                            .replace(/^## (.*$)/gm, '<h2 class="text-xl font-semibold mb-3 mt-6 text-gray-800">$1</h2>')
                            .replace(/^### (.*$)/gm, '<h3 class="text-lg font-medium mb-2 mt-4 text-gray-700">$1</h3>')
                            .replace(/\|(.*?)\|/g, (match, content) => {
                              const cells = content.split('|').map(cell => cell.trim());
                              return `<div class="table-row flex border-b border-gray-200 py-2">${cells.map(cell => 
                                `<div class="table-cell flex-1 px-2">${cell}</div>`
                              ).join('')}</div>`;
                            })
                        }}
                      />
                    </div>
                  </div>
                  
                  <div className="mt-6 pt-6 border-t border-gray-100">
                    <div className="flex items-center justify-between text-sm text-gray-500">
                      <span>Generated by AI Trip Planner</span>
                      <div className="flex items-center space-x-1">
                        <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                        <span>Ready to travel</span>
                      </div>
                    </div>
                  </div>
                </div>
              )}
              
              {!travelPlan && !error && !isLoading && (
                <div className="bg-white rounded-2xl shadow-xl p-8 text-center">
                  <div className="w-16 h-16 bg-gradient-to-r from-blue-100 to-purple-100 rounded-full flex items-center justify-center mx-auto mb-4">
                    <Plane className="w-8 h-8 text-blue-600" />
                  </div>
                  <h3 className="text-xl font-semibold text-gray-800 mb-2">Ready to Plan?</h3>
                  <p className="text-gray-600">Fill out the form to get your personalized AI-generated travel itinerary from our live backend.</p>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;