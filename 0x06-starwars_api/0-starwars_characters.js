#!/usr/bin/node

const axios = require('axios');
const process = require('process');

function getMovieCharacters(movieId) {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

    axios.get(url)
        .then(response => {
            const characters = response.data.characters;
            characters.forEach(characterUrl => {
                axios.get(characterUrl)
                    .then(response => {
                        console.log(response.data.name);
                    });
            });
        });
}

const movieId = process.argv[2];
getMovieCharacters(movieId);
