#!/usr/bin/node
const request = require('request-promise');

async function getFilmCharacters () {
  try {
    const filmResponse = await request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`);
    const filmBody = JSON.parse(filmResponse);
    const characters = filmBody.characters;
    const listNamesPromises = characters.map(async (characterUrl) => {
      const characterResponse = await request(characterUrl);
      const characterBody = JSON.parse(characterResponse);
      return characterBody.name;
    });

    // Await all promises resolved (i.e., all requests completed)
    const listNames = await Promise.all(listNamesPromises);
    listNames.forEach(element => {
      console.log(element);
    });
    // Correctly logs all names after they've been fetched
  } catch (error) {
    console.error('Error fetching data:', error.message);
  }
}

getFilmCharacters();
