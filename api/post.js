
import { Client } from "@gradio/client";

const client = Client.connect("KingNish/OpenGPT-4o");

export default async function handler(req, res) {
    if (req.method === 'POST') {
      // Get data from the request body
      const prompt = req.body;

    const result = client.predict("/chat", { 		
		user_prompt: {"text": prompt,"files":[]}, 
    });
  
      // Respond with a success message
      res.status(200).json({ result: result.data });
    } else {
      // If not a POST request, return a 405 method not allowed
      res.setHeader('Allow', ['POST']);
      res.status(405).end(`Method ${req.method} Not Allowed`);
    }
  }
  