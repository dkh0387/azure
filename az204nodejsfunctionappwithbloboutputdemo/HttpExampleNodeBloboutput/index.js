module.exports = async function (context, req) {
    const name = req.query.name || (req.body && req.body.name);

    context.bindings.outputBlob = `Hallo ${name}, dies ist der Blob-Inhalt`;

    context.res = {
        status: 200,
        body: name
            ? `Hallo, ${name}!`
            : "Bitte gib einen Namen in der URL oder im Body an (name=...)"
    };
};
