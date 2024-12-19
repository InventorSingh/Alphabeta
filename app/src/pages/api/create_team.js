export async function post({ request }) {
    const formData = await request.formData();
    const teamName = formData.get('teamName');
    const services = formData.get('services');
    const contactEmail = formData.get('contactEmail');
  
    // You can add logic to save the data (e.g., in a database or a file)
    console.log({ teamName, services, contactEmail });
  
    return new Response(null, {
      status: 302,
      headers: {
        Location: '/featured-teams', // Redirect to a page after submission
      },
    });
  }
  