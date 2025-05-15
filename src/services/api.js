const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

export const getFormStructure = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}`);
    if (!response.ok) {
      throw new Error('Failed to fetch form structure');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching form structure:', error);
    throw error;
  }
};

export const submitFormData = async (formData) => {
  try {
    const response = await fetch(`${API_BASE_URL}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    });
    
    if (!response.ok) {
      throw new Error('Form submission Failed');
    }
    return await response.json();
  } catch (error) {
    console.error('Error submitting form:', error);
    throw error;
  }
};