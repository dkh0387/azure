using Azure.Identity;
using Microsoft.Graph;
using Microsoft.Graph.Models;
using System;
using System.Threading.Tasks;



namespace GraphAPIConsoleApp

{

    internal class Program

    {

        public async static Task Main(string[] args)
        {
            var scopes = new[] { "https://graph.microsoft.com/.default" };
            var tenantId = "1fe56840-7d66-45e7-931e-3751441409b5";
            var clientId = "c0f4b916-0fe6-4d63-b774-ff615dbdef6d";
            var clientSecret = ".bL8Q~nA8S5eKGQxm~h6sdjkTLyuYhm~fDfI.b59";

            var options = new TokenCredentialOptions
            {
                AuthorityHost = AzureAuthorityHosts.AzurePublicCloud
            };

            var clientSecretCredential = new ClientSecretCredential(tenantId, clientId, clientSecret, options);

            var graphClient = new GraphServiceClient(clientSecretCredential, scopes);

            UserCollectionResponse? users = await graphClient.Users.GetAsync();

            foreach (var user in users.Value)
            {
                Console.WriteLine($"User DisplayName: {user.DisplayName}");
            }

        }

    }

}